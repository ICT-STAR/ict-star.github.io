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
          section: "News",},{id: "people-haowenli",
          title: 'Haowenli',
          description: "",
          section: "People",handler: () => {
              window.location.href = "/people/haowenli.html";
            },},{id: "people-jiajun",
          title: 'Jiajun',
          description: "",
          section: "People",handler: () => {
              window.location.href = "/people/jiajun.html";
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
            },},{id: "projects-model-editing",
          title: 'Model Editing',
          description: "Model Editing.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/example/";
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