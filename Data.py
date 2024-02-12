from win32gui import LoadIcon


class Data:
    """
    该类定义了 Dustborn 执行过程中可能需要用到的数据。
    """
    windows = (

        # 作者网页
        "https://bilibili.com/182330206",

        # SEA ABYSS，来自一首诗
        "https://www.bing.com/search?q=%E5%9D%A0%E8%90%BD%E3%80%82%E5%A5%B9%E5%B0%86%E4%BD%99%E5%85%89%E5%86%8D%E6%AC"
        "%A1%E6%B4%92%E5%90%91%E6%9C%80%E5%90%8E%E5%91%88%E7%8E%B0%E7%9A%84%E3%80%8C%E6%B5%B7%E5%BA%95%E6%B7%B1%E6%B8"
        "%8A%E3%80%8D",
        "https://www.sogou.com/web?query=%E4%BA%8E%E6%AD%A4%E5%A4%84%E3%80%82%E9%BB%91%E9%82%83%E7%9A%84%E6%B7%B1%E6"
        "%B8%8A",
        "https://www.so.com/s?q=%E4%BA%BA%E4%BB%AC%E7%94%A8%E8%83%8C%E8%BF%9E%E6%88%90%E9%BB%91%E9%82%83%E7%9A%84%E6"
        "%B7%B1%E6%B8%8A%E5%A3%81+%E8%80%8C%E8%83%8C%E6%9C%9D%E9%BB%91%E9%82%83%E7%9A%84%E6%B7%B1%E6%B8%8A",
        "https://www.wuzhuiso.com/s?q=%E6%97%A0%E6%95%B0%E5%B7%B2%E7%BB%8F%E6%AE%8B%E7%A0%B4%E7%9A%84%E7%A2%8E%E7%89"
        "%87+%E5%A6%82%E5%85%89%E9%B2%9C%E4%BA%AE%E4%B8%BD%E7%9A%84%E6%B2%B9%E6%BC%86%E6%9D%BF",
        "https://quark.sm.cn/s?q=%E5%9C%A8%E6%B7%B1%E6%B5%B7%E4%B8%AD%20%E5%9C%A8%E4%BA%BA%E4%BB%AC%E7%9A%84%E7%9C%BC"
        "%E5%89%8D%E6%9E%84%E9%80%A0%E4%BB%85%E9%99%86%E5%9C%B0%E4%B8%8A%E5%8F%AF%E8%A7%81%E7%9A%84%20%E7%BF%94%E5%AE"
        "%9E%E7%9A%84%E8%93%9D%E5%9B%BE&safe=1",
        "https://so.toutiao.com/search?dvpf=pc&source=input&keyword=%E6%B3%A8%E5%AE%9A%E6%97%A0%E4%BE%9D%E3%80%82%E6"
        "%AE%8B%E7%A0%B4%E7%9A%84%E4%B8%AA%E4%BD%93%E5%9C%A8%E8%87%AA%E7%94%B1%E8%90%BD%E4%BD%93%E4%B8%AD%E5%B0%86%E8"
        "%87%AA%E8%BA%AB%E8%A7%A3%E6%9E%84",
        "https://yandex.com/search/?text=%E8%BA%AB%E8%BA%AF%E7%A9%BF%E6%A2%AD%E5%9C%A8%E6%B6%B2%E5%92%8C%E6%B0%94%E4"
        "%B8%AD+%E5%B0%86%E6%B7%B7%E5%90%88%E7%89%A9%E5%88%92%E5%87%BA%E4%BA%86%E7%AC%91%E5%A3%B0%E8%88%AC%E7%9A%84"
        "%E5%B0%96%E9%94%90",
        "https://fsoufsou.com/search?q=%E6%80%9D%E6%83%B3%E9%9A%8F%E7%89%A9%E8%B4%A8%E7%9A%84%E6%B9%AE%E7%81%AD%E8%80"
        "%8C%E6%B9%AE%E7%81%AD&tbn=all",
        "https://backdata.net/search.html?q=%E7%9B%B4%E5%88%B0%E6%B0%94%E5%8E%8B%E8%AE%A9%E5%A5%B9%E7%9A%84%E8%BA%AB"
        "%E4%BD%93%E6%94%AF%E7%A6%BB%E7%A0%B4%E7%A2%8E%20%E8%A1%80%E6%BB%B4%E6%B7%B7%E7%9D%80%E7%B2%89%E6%9C%AB%E7%BB"
        "%88%E6%9C%AB%E6%89%A9%E6%95%A3%E5%9C%A8%E8%BF%99%E6%B5%B7%E4%B8%AD&page=1",
        "https://ffsou.com/so/%E9%82%A3%E6%98%AF%E7%A2%8E%E7%89%87%E3%80%82%E4%BC%98%E9%9B%85%E7%9A%84%E7%A2%8E%E7%89"
        "%87%E6%9E%84%E9%80%A0%E6%B2%B9%E6%BC%86%E6%9D%BF%EF%BC%8C%E5%B9%B3%E5%AE%9E%E7%9A%84%E7%A2%8E%E7%89%87%E5%90"
        "%91%E4%B8%8B%E7%BB%A7%E7%BB%AD%E5%9D%A0%E8%90%BD%E3%80%82",
        "https://swisscows.com/en/web?query=%E6%97%A0%E4%BA%BA%E7%9F%A5%E6%99%93%E9%82%A3%E7%A2%8E%E7%89%87%E6%98%AF"
        "%E5%90%A6%E8%A7%A6%E5%BA%95%E3%80%82",
        "https://startgoogle.startpagina.nl/?origin=homepage&query=%E6%97%A0%E7%9F%A5%E7%9A%84%E6%B7%B1%E6%B8%8A%E5"
        "%A3%81%E5%8E%8C%E6%81%B6%E4%BA%86%E6%B2%B9%E6%BC%86%E6%9D%BF+%E4%BB%96%E4%BB%AC%E5%90%91%E8%87%AA%E5%B7%B1"
        "%E7%9A%84%E6%94%AF%E7%A6%BB%E7%A0%B4%E7%A2%8E%E7%9A%84%E5%86%85%E5%BF%83%E7%AA%A5%E8%A7%91",
        "https://www.wolframalpha.com/input?i=%E7%9B%B4%E5%88%B0%E8%87%AA%E5%B7%B1%E4%B9%9F%E6%B9%AE%E6%B2%A1%E5%9C"
        "%A8%E6%B2%B9%E6%BC%86%E4%B8%AD%E3%80%82",

        # 帮助类网页
        "https://reddit.com/r/askreddit",
        "https://tieba.baidu.com",
        "https://bing.com/search?q=%E7%B3%BB%E7%BB%9F%E6%96%87%E4%BB%B6%E6%8D%9F%E5%9D%8F%E5%A6%82%E4%BD%95%E4%BF%AE"
        "%E5%A4%8D",
        "https://www.bing.com/search?q=%E7%94%B5%E8%84%91%E8%93%9D%E5%B1%8F%E6%97%A0%E6%B3%95%E5%BC%80%E6%9C%BA",
        "https://www.bing.com/search?q=Python+%E7%97%85%E6%AF%92%E4%B8%8B%E8%BD%BD",
        "https://www.bing.com/search?q=virus.exe",
        "https://www.bing.com/search?q=IE+%E6%B5%8F%E8%A7%88%E5%99%A8%E6%98%AF%E6%9C%80%E5%A5%BD%E7%9A%84",
        "https://www.bing.com/search?q=%E5%A6%82%E4%BD%95%E9%BB%91%E5%85%A5+QQ",
        "https://www.bing.com/search?q=https://www.bing.com/search?q=%E5%8D%A1%E5%B7%B4%E6%96%AF%E5%9F%BA%E5%85%8D%E8"
        "%B4%B9%E7%89%88%E4%B8%8B%E8%BD%BD",
        "https://www.bing.com/search?q=%E5%A6%82%E4%BD%95%E8%87%AA%E5%88%B6%E7%97%85%E6%AF%92",

        # 系统工具
        "calc",
        "notepad",
        "cmd",
        "write",
        "regedit",
        "explorer",
        "taskmgr",
        "msconfig",
        "mspaint",
        "devmgmt.msc",
        "control",
        "mmc",
        "osk",
        "winver",
    )

    warning_icon = LoadIcon(None, 32515)  # type: ignore
    error_icon = LoadIcon(None, 32513)  # type: ignore
