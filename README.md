# 使用指南

## About

- 内容: 修改`/_pages/about.md`
- 图片: 修改`_data/carousel.yml`
  - 需要填写：
    - `image`：图片名称，如`1.jpg`，置于`/assets/img/carousel/`文件夹下
    - `caption`：图片描述
  - 图片按照填写顺序展示

## News

- 在`_news/`文件夹下创建新的markdown文件，如`announcement_1.md`
  - 模板如下：
    ```
    ---
    layout: post
    date: 2015-10-22 15:59:00
    inline: true
    related_posts: false
    ---
    内容
    ```

## People

- 在`_people/`文件夹下创建新的markdown文件，如`zhangsan.md`，模板如下：
  ```
  ---
  name: San Zhang
  photo: zhangsan.jpg (置于`/assets/img/people/`文件夹下)
  info: Associate Professor
  research_interests:
    - Large language Models
    - Recommendation Systems
    - Graph Neural Networks
  category: faculty (可选：faculty, phd, master, undergraduate)
  (下面链接为可选项)
  homepage: https://example.com
  email: example@example.com
  google_scholar: https://scholar.google.com/citations?user=example
  github: https://github.com/example
  facebook: https://www.facebook.com/example
  x: https://x.com/example
  linkedin: https://www.linkedin.com/in/example
  ---
  ```

## Projects

- 在`_projects/`文件夹下创建新的markdown文件，如`project_1.md`
  - 模板如下：
    ```
    ---
    layout: project
    title: "example"
    author:
    - San Zhang
    - Si Li
    description: example
    img: example.png (封面图片，置于`/assets/img/project/cover/`文件夹下)
    time: 2024-01-02 15:59:00
    ---
    网页内容
    ```

## Publications

- 编辑`_bibliography/papers.bib`文件
  - 模板如下：
    ```
    @article{PhysRev.47.777,
    abbr={PhysRev},
    title={Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?},
    author={Einstein*†, A. and Podolsky*, B. and Rosen*, N.},
    abstract={In a complete theory there is an element corresponding to each element of reality. A sufficient condition for the reality of a physical quantity is the possibility of predicting it with certainty, without disturbing the system. In quantum mechanics in the case of two physical quantities described by non-commuting operators, the knowledge of one precludes the knowledge of the other. Then either (1) the description of reality given by the wave function in quantum mechanics is not complete or (2) these two quantities cannot have simultaneous reality. Consideration of the problem of making predictions concerning a system on the basis of measurements made on another system that had previously interacted with it leads to the result that if (1) is false then (2) is also false. One is thus led to conclude that the description of reality as given by a wave function is not complete.},
    journal={Phys. Rev.},
    location={New Jersey},
    volume={47},
    issue={10},
    pages={777--780},
    numpages={0},
    year={1935},
    month={May},
    publisher=aps,
    doi={10.1103/PhysRev.47.777},
    url={http://link.aps.org/doi/10.1103/PhysRev.47.777},
    html={https://journals.aps.org/pr/abstract/10.1103/PhysRev.47.777}, # 添加论文页面
    github={https://github.com/alshedivat/al-folio/}, # 添加github链接
    pdf={example_pdf.pdf}, # 添加pdf文件，置于`/assets/pdf/`文件夹下
    google_scholar_id={qyhmnyLat1gC}, # 添加google scholar id，用于引用计数
    video={https://www.youtube-nocookie.com/embed/aqz-KE-bpKQ}, # 添加视频链接
    additional_info={. *More Information* can be [found here](https://github.com/alshedivat/al-folio/)}, # 添加额外信息，位于期刊名称旁
    annotation={* Example use of superscripts<br>† Albert Einstein}, # 添加注释，位于作者旁
    }
    ```

## Funding

- 文案：`_pages/funding.md`
- 机构logo：`_data/funding.yml`
  - 需要填写：
    - `logo`：机构logo名称，如`example.png`，置于`/assets/img/funding/`文件夹下
    - `name`：机构名称
    - `url`：机构链接

## Join Us

- 内容：`_pages/join_us.md`

## Markdown说明

- 公式：
  - 行内公式：使用`$$`包裹公式，如`$$E=mc^2$$`
  - 块级公式：使用`$$`包裹公式，并另起一行，如
    ```
    $$
    E=mc^2
    $$
    ```
- 图片：
  - 格式1：`![alt](url)`，如`![example](assets/img/example.png)`，
  - 格式2：`{% include figure.liquid path="example.png" alt="example" %}`，如`{% include figure.liquid path="example.png" alt="example" %}`
  - 图注: `<div class="caption">图注</div>`

- 脚注：
  - 在需要添加脚注的地方添加`[^index]`，如`[^1]`
  - 在markdown底部添加脚注：
    ```
    ---
    [^1]: 脚注内容
    ```
