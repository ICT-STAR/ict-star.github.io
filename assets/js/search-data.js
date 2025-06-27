// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-home",
    title: "Home",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-news",
          title: "news",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/news/";
          },
        },{id: "nav-people",
          title: "people",
          description: "members of the lab or group",
          section: "Navigation",
          handler: () => {
            window.location.href = "/people/";
          },
        },{id: "nav-projects",
          title: "projects",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "nav-seminars",
          title: "seminars",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/seminars/";
          },
        },{id: "nav-publications",
          title: "publications",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-funding",
          title: "funding",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/funding/";
          },
        },{id: "nav-join-us",
          title: "join us",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/join_us/";
          },
        },{id: "news-our-paper-unlink-to-unlearn-simplifying-edge-unlearning-in-gnns-is-accepted-by-webconf2024-congrats-to-jiajun",
          title: 'Our paper Unlink to Unlearn: Simplifying Edge Unlearning in GNNs is accepted by...',
          description: "",
          section: "News",},{id: "news-three-papers-are-accepted-by-acl2024-about-model-editing-bias-in-knowledge-conflict-and-confidence-alignment-congrats-to-hexiang-wanli-and-shuchang",
          title: 'Three papers are accepted by ACL2024 about model editing, bias in knowledge conflict,...',
          description: "",
          section: "News",},{id: "news-our-paper-the-fall-of-rome-is-accepted-by-emnlp2024-finding-congrats-to-wanli",
          title: 'Our paper The Fall of ROME is accepted by EMNLP2024 finding. Congrats to...',
          description: "",
          section: "News",},{id: "news-we-will-hold-the-1st-workshop-on-human-centered-recommender-systems-on-www-25-contributions-are-welcome",
          title: 'We will hold The 1st Workshop on Human-Centered Recommender Systems on WWW 25....',
          description: "",
          section: "News",},{id: "news-two-papers-are-accepted-by-acl2025-about-model-editing-and-watermarking-congrats-to-wanli-and-beining",
          title: 'Two papers are accepted by ACL2025 about model editing and watermarking. Congrats to...',
          description: "",
          section: "News",},{id: "people-chenzhenxing",
          title: 'Chenzhenxing',
          description: "",
          section: "People",handler: () => {
              window.location.href = "/people/chenzhenxing.html";
            },},{id: "people-haowenli",
          title: 'Haowenli',
          description: "",
          section: "People",handler: () => {
              window.location.href = "/people/haowenli.html";
            },},{id: "people-jiajun",
          title: 'Jiajun',
          description: "",
          section: "People",handler: () => {
              window.location.href = "/people/jiajun.html";
            },},{id: "people-pujiayue",
          title: 'Pujiayue',
          description: "",
          section: "People",handler: () => {
              window.location.href = "/people/pujiayue.html";
            },},{id: "people-shaliu",
          title: 'Shaliu',
          description: "",
          section: "People",handler: () => {
              window.location.href = "/people/shaliu.html";
            },},{id: "people-sunfei",
          title: 'Sunfei',
          description: "",
          section: "People",handler: () => {
              window.location.href = "/people/sunfei.html";
            },},{id: "people-tangrui",
          title: 'Tangrui',
          description: "",
          section: "People",handler: () => {
              window.location.href = "/people/tangrui.html";
            },},{id: "people-tanhexiang",
          title: 'Tanhexiang',
          description: "",
          section: "People",handler: () => {
              window.location.href = "/people/tanhexiang.html";
            },},{id: "people-wanli",
          title: 'Wanli',
          description: "",
          section: "People",handler: () => {
              window.location.href = "/people/wanli.html";
            },},{id: "people-xunliu",
          title: 'Xunliu',
          description: "",
          section: "People",handler: () => {
              window.location.href = "/people/xunliu.html";
            },},{id: "people-zongdanyang",
          title: 'Zongdanyang',
          description: "",
          section: "People",handler: () => {
              window.location.href = "/people/zongdanyang.html";
            },},{id: "projects-model-editing",
          title: 'Model Editing',
          description: "Model Editing.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/example/";
            },},{id: "seminars-example",
          title: 'example',
          description: "",
          section: "Seminars",handler: () => {
              window.location.href = "/seminars/example/";
            },},{id: "seminars-reasoning-errors-of-llms",
          title: 'Reasoning Errors of LLMs',
          description: "",
          section: "Seminars",handler: () => {
              window.location.href = "/seminars/reasoning_error_of_LLMs_Wanli/";
            },},{id: "seminars-rethinking-llm-unlearning-benchmarks-and-datasets",
          title: 'Rethinking LLM Unlearning: Benchmarks and Datasets',
          description: "",
          section: "Seminars",handler: () => {
              window.location.href = "/seminars/rethinking_LLM_unlearning_qrc/";
            },},{id: "seminars-towards-robust-safety-alignment-of-llms",
          title: 'Towards Robust Safety Alignment of LLMs',
          description: "",
          section: "Seminars",handler: () => {
              window.location.href = "/seminars/robust_alignment_LLMs/";
            },},{id: "seminars-rethinking-self-consistency-for-hallucination-detection-in-llms",
          title: 'Rethinking Self-Consistency for Hallucination Detection in LLMs',
          description: "",
          section: "Seminars",handler: () => {
              window.location.href = "/seminars/self-consistency_ls/";
            },},{id: "seminars-ai-scheming-frontier-models-may-pursue-secret-goals-and-lie-to-you",
          title: 'AI Scheming: Frontier Models may Pursue Secret Goals and Lie to You',
          description: "",
          section: "Seminars",handler: () => {
              window.location.href = "/seminars/ai_scheming_xun/";
            },},{id: "seminars-relearn-unlearning-via-learning-for-large-language-models",
          title: 'ReLearn: Unlearning via Learning for Large Language Models',
          description: "",
          section: "Seminars",handler: () => {
              window.location.href = "/seminars/ReLearn_paperReading_honglin/";
            },},{id: "seminars-llms-in-recommender-system",
          title: 'LLMs in Recommender System',
          description: "",
          section: "Seminars",handler: () => {
              window.location.href = "/seminars/LLMs_in_Recsys_Wenwei/";
            },},{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
