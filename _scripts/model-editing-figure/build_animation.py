"""Rebuild the project page animation from the preserved TikZ artwork."""
from pathlib import Path
import copy
import json
import math
import re
import xml.etree.ElementTree as ET

BASE = Path(__file__).resolve().parent
BUILD = BASE / "build"
BUILD.mkdir(exist_ok=True)
PUBLIC_SVG = BASE.parent.parent / "assets/img/project/model-editing/mirage-fig3-animated.svg"
SVG = "http://www.w3.org/2000/svg"
XLINK = "http://www.w3.org/1999/xlink"
ET.register_namespace("", SVG)
ET.register_namespace("xlink", XLINK)
DURATION = 28.0
BOUNDS = (-5.133855, 265.528847, 456.742875, 167.601056)


def tag(name):
    return "{" + SVG + "}" + name


root = ET.parse(BASE / "source/semantic-base.svg").getroot()
root.set("id", "mirage-animation")
root.set("viewBox", " ".join(str(v) for v in BOUNDS))
root.set("width", "1800")
root.set("height", str(round(1800 * BOUNDS[3] / BOUNDS[2], 3)))
root.set("role", "img")
root.set("aria-labelledby", "animation-title animation-description")
title = ET.Element(tag("title"), id="animation-title")
title.text = "Model editing evaluation: teacher forcing versus autoregressive decoding"
desc = ET.Element(tag("desc"), id="animation-description")
desc.text = (
    "Original paper artwork animated in paired steps. Both models first predict Beyoncé. "
    "Synthetic evaluation then supplies BC from the reference answer; WILD feeds back its own Beyoncé. "
    "After five steps, synthetic evaluation compares positions, giving cross, check, cross, check, check "
    "and three out of five. WILD stops at EOS and judges the entire answer incorrect, score zero."
)
root.insert(0, title)
root.insert(1, desc)
style = ET.Element(tag("style"))
style.text = """
@media (prefers-reduced-motion: reduce) {
  svg:not(.motion-enabled) .anim-layer { opacity: 1 !important; }
  svg:not(.motion-enabled) .draw-reveal { stroke-dasharray: none !important; stroke-dashoffset: 0 !important; }
}
"""
root.insert(2, style)
defs = root.find(tag("defs"))
background = ET.Element(tag("rect"), {
    "x": str(BOUNDS[0]), "y": str(BOUNDS[1]),
    "width": str(BOUNDS[2]), "height": str(BOUNDS[3]), "fill": "#ffffff",
})
root.insert(list(root).index(defs) + 1, background)

# Two source nodes lacked explicit TikZ names. Identify the original vector elements.
parents = {child: parent for parent in root.iter() for child in parent}
for use in root.iter(tag("use")):
    if use.get("{" + XLINK + "}href") == "#g21-205" and use.get("x") == "10.42178":
        ancestors = []
        node = use
        while node in parents:
            node = parents[node]
            ancestors.append(node)
        if not any(n.get("id", "").startswith(("syn-", "wild-")) for n in ancestors):
            next(n for n in ancestors if "transform" in n.attrib).set("id", "syn-metric-label")
for group in root.iter(tag("g")):
    if group.get("fill") == "#f59b99" and any(
        p.get("d", "").startswith("M200.16147 68.56036H178.07153") for p in group.findall(tag("path"))
    ):
        group.set("id", "wild-eos-background")

elements = {el.get("id"): el for el in root.iter() if el.get("id")}
curves = []
events = []
counter = 0


def identify(el, prefix="animated-part"):
    global counter
    if not el.get("id"):
        counter += 1
        el.set("id", prefix + "-" + str(counter))
        elements[el.get("id")] = el
    return el.get("id")


def curve(el, attribute, times, values):
    identity = identify(el)
    el.set(attribute, str(values[0]))
    ET.SubElement(el, tag("animate"), {
        "attributeName": attribute, "dur": "28s", "repeatCount": "indefinite",
        "values": ";".join(str(v) for v in values),
        "keyTimes": ";".join(format(t / DURATION, ".8f") for t in times),
        "calcMode": "linear",
    })
    curves.append({"id": identity, "attribute": attribute, "times": times, "values": values})


def reveal(el, start, fade=0.12):
    if isinstance(el, str):
        el = elements[el]
    el.set("class", (el.get("class", "") + " anim-layer").strip())
    curve(el, "opacity", [0, start, start + fade, 27, 28], [0, 0, 1, 1, 0])


def shaft_length(data):
    """Length of this figure's M/L/H/V/C arrow paths in their native SVG units."""
    tokens = re.findall(r"[A-Za-z]|[-+]?(?:\d*\.\d+|\d+\.?\d*)(?:[eE][-+]?\d+)?", data)
    position = (0.0, 0.0)
    command = ""
    index = 0
    length = 0.0
    while index < len(tokens):
        if tokens[index].isalpha():
            command = tokens[index]
            index += 1
        assert command in ("M", "L", "H", "V", "C"), command
        count = {"M": 2, "L": 2, "H": 1, "V": 1, "C": 6}[command]
        values = [float(v) for v in tokens[index:index + count]]
        index += count
        if command == "M":
            position = tuple(values)
            command = "L"
            continue
        if command == "C":
            p0, p1, p2, p3 = position, tuple(values[:2]), tuple(values[2:4]), tuple(values[4:])
            for part in range(1, 33):
                t = part / 32
                point = tuple((1-t)**3*p0[k] + 3*(1-t)**2*t*p1[k] + 3*(1-t)*t*t*p2[k] + t**3*p3[k] for k in (0, 1))
                length += math.dist(position, point)
                position = point
        else:
            point = tuple(values) if command == "L" else (values[0], position[1]) if command == "H" else (position[0], values[0])
            length += math.dist(position, point)
            position = point
    return length


def grow(identity, start, length, judgments=False):
    group = elements[identity]
    reveal(group, start, 0.05)
    paths = list(group.iter(tag("path")))
    shafts = [p for p in paths if p.get("fill") == "none"]
    assert shafts, identity + " has no shaft"
    for path in shafts:
        number = len(curves)
        mask_id = "draw-mask-" + str(number)
        distance = shaft_length(path.get("d"))
        mask = ET.SubElement(defs, tag("mask"), {
            "id": mask_id, "maskUnits": "userSpaceOnUse",
            "x": "-1000", "y": "-1000", "width": "2000", "height": "2000",
            "style": "mask-type:luminance",
        })
        line = ET.SubElement(mask, tag("path"), {
            "d": path.get("d"), "fill": "none", "stroke": "#fff",
            "stroke-width": "5", "stroke-linecap": "butt",
            "stroke-dasharray": str(distance) + " " + str(distance), "class": "draw-reveal",
        })
        if path.get("transform"):
            line.set("transform", path.get("transform"))
        curve(line, "stroke-dashoffset", [0, start, start + length, 28], [distance, distance, 0, 0])
        path.set("mask", "url(#" + mask_id + ")")
    for head in [p for p in paths if p not in shafts]:
        reveal(head, start + length, 0.07)
    if judgments:
        for glyph in list(group.iter(tag("use"))):
            reveal(glyph, start + length + 0.08, 0.1)
    events.append({"id": identity, "start": start, "end": start + length, "kind": "arrow"})


for panel in ("syn", "wild"):
    reveal(panel + "-input-0", 0.2)
    grow(panel + "-in-arrow-0", 2.0, 0.6)
    grow(panel + "-out-arrow-0", 2.85, 0.6)
    reveal(panel + "-output-0", 3.55)
    for step in range(1, 5):
        start = 4.8 + (step - 1) * 3
        grow(panel + "-feedback-" + str(step), start, 0.9)
        reveal(panel + "-input-" + str(step), start + 0.9)
        grow(panel + "-in-arrow-" + str(step), start + 1.1, 0.55)
        grow(panel + "-out-arrow-" + str(step), start + 1.9, 0.55)
        reveal(panel + "-output-" + str(step), start + 2.55)
    for suffix in ("method-summary", "output-box", "output-label"):
        reveal(panel + "-" + suffix, 16.65)
    grow(panel + "-stop-path", 17.0, 1.0)
    reveal(panel + "-stop-label", 17.1)
    reveal(panel + "-stop-sign", 18.05)

reveal("wild-eos-background", 16.35)
reveal("syn-groundtruth-box", 16.65)
for identity in ("wild-groundtruth", "wild-groundtruth-label", "wild-groundtruth-box"):
    reveal(identity, 18.5)
for identity in ("syn-metric-label", "syn-metric-metric"):
    reveal(identity, 19.0)
grow("syn-metric-arrow-2", 18.8, 0.55)
grow("syn-metric-arrow-3", 19.0, 0.55)
for step in range(5):
    grow("syn-match-" + str(step), 19.0 + step * 0.55, 0.32, judgments=True)
reveal("syn-metric-m-box", 21.7)
grow("syn-metric-arrow-0", 22.1, 0.5)
grow("syn-metric-arrow-1", 22.1, 0.5)
reveal("syn-metric-result", 22.7)
for identity in ("wild-metric-metric", "wild-metric-metric-label",
                 "wild-metric-metric-label1", "wild-metric-metric-an"):
    reveal(identity, 19.0)
grow("wild-metric-arrow-1", 19.0, 0.6)
grow("wild-metric-arrow-2", 19.2, 0.6)
grow("wild-metric-arrow-0", 22.1, 0.5)
reveal("wild-metric-result", 22.7)

STAGES = [
    [0, "从模型框架开始。左侧标准答案可用于 teacher forcing；右侧生成时不读取标准答案。"],
    [2, "第 1 步：<BOS> 输入模型，随后模型给出第一个预测。"],
    [3.55, "两侧都先预测 Beyoncé。下一步的输入来源将开始分岔。"],
    [4.8, "左：从标准答案取 BC；右：把自己的 Beyoncé 送回模型。"],
    [7.35, "第 2 个输出出现：左侧 Jean，右侧 is。"],
    [7.8, "下一步：左侧喂入标准答案 Jean；右侧喂入自己的 is。"],
    [10.35, "第 3 个输出：左侧 is，右侧 the。"],
    [10.8, "下一步：左侧喂入标准答案 and；右侧喂入自己的 the。"],
    [13.35, "第 4 个输出：左侧 Toby，右侧 writer。"],
    [13.8, "最后一步：左侧喂入标准答案 Toby；右侧喂入自己的 writer。"],
    [16.35, "第 5 个输出：左侧 Gad，右侧结束标记 <|endoftext|>。"],
    [16.65, "五步输入输出完成：用输出框、大括号和②标注总结两种生成流程。"],
    [17, "停止规则：左侧按标准答案的 5 个 token 截断；右侧遇到结束标记后自然停止。"],
    [18.5, "生成结束后开始评分。WILD 此时才把参考答案送给评判器。"],
    [19.4, "逐位置比较①：Beyoncé ≠ BC，暂时 0/1。"],
    [19.95, "逐位置比较②：Jean = Jean，暂时 1/2。"],
    [20.5, "逐位置比较③：is ≠ and，暂时 1/3。"],
    [21.05, "逐位置比较④：Toby = Toby，暂时 2/4。"],
    [21.6, "逐位置比较⑤：Gad = Gad，累计 3/5。"],
    [22.7, "最终评分：左侧 token 匹配率 3/5；右侧完整回答不正确，判为 0。"],
    [23, "保留完整原图：左侧的部分 token 匹配，不等于整个事实回答正确。"],
    [27, "一轮演示完成；继续播放将收起动态层，并从模型框架重新开始。"],
]
STEPS = [0.5, 3.8, 7.6, 10.6, 13.6, 16.6, 16.9, 18.3, 19.8, 20.35, 20.9, 21.45, 21.95, 22.95, 25]
manifest = {"duration": DURATION, "curves": curves, "events": events, "stages": STAGES, "steps": STEPS}
(BUILD / "timeline.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
metadata = ET.SubElement(root, tag("metadata"), id="animation-timing")
metadata.text = json.dumps({"duration": DURATION})
animated = ET.tostring(root, encoding="unicode")
PUBLIC_SVG.write_text('<?xml version="1.0" encoding="UTF-8"?>\n' + animated)
template = (BASE / "source/player-template.html").read_text()
template = template.replace("<!--ANIMATED_SVG-->", animated)
template = template.replace("/*TIMELINE_DATA*/", json.dumps({"duration": DURATION, "stages": STAGES, "steps": STEPS}, ensure_ascii=False))
(BUILD / "mirage-fig3-player.html").write_text(template)


def interpolate(times, values, time):
    for i in range(1, len(times)):
        if time <= times[i]:
            fraction = (time - times[i - 1]) / (times[i] - times[i - 1])
            return values[i - 1] + max(0, min(1, fraction)) * (values[i] - values[i - 1])
    return values[-1]


def freeze(time, destination):
    static = copy.deepcopy(root)
    nodes = {e.get("id"): e for e in static.iter() if e.get("id")}
    for item in curves:
        value = interpolate(item["times"], item["values"], time % DURATION)
        nodes[item["id"]].set(item["attribute"], format(value, ".8f"))
    for parent in static.iter():
        for child in list(parent):
            if child.tag == tag("animate"):
                parent.remove(child)
    destination.write_text(ET.tostring(static, encoding="unicode"))


for time in (0.8, 2.3, 3.8, 5.3, 7.6, 16.6, 16.9, 19.4, 21.6, 25):
    freeze(time, BUILD / ("frame-" + str(time).replace(".", "-") + ".svg"))
print("Built animated SVG, standalone player, and inspection frames.")
