# Python
用来说明2019-2020学年Python课程期末项目
## Welcome to Xiaofeng ＆ Python

```markdown
本文档主要根据评分细则来进行说明期末项目，如果有描述不当的地方请见谅。
```
### pythonanywhere地址：[http://xiaofeng0418.pythonanywhere.com/](http://xiaofeng0418.pythonanywhere.com/)
### URL数量总共为六个

### HTML档描述
在pycharm内通过render、return、plot_all等代码函数，对python档和HTML档进行了数据交互，使得数据的可视化图表能够正常显示并且部署到pythonanywhere上。HTML档有加过滤器（eg：{{the_fenshenggdp|safe}}）让数据能正常交互。
```markdown
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{{the_fenshenggdp|safe}}
</body>
</html>
```

### Python档描述
Python档内，先是通过from import as引入对应所需要的模块，之后用def returm for in等引入数据可视化格式等，最后是进行了与html档的交互，最终形成一个python档，在分别完成相对应的python档后，我就将所有的python档进行整合，便于后续的步骤进行。


### 交互功能
1. 数据的可视化具有交互功能，无论是条形图、线形图还是地图等都可以进行数据筛选的交互功能。
2. 有数据筛选的按钮，可以根据需要选择需要的数据类型。
3. 可以切换不同表格的按钮
### 数据交互（以其中一个代码片段举例）
```markdown
def bar() -> 'html':
    df = pd.read_csv('quanguofeiqi.csv')
    line = (
    Line()
    .add_xaxis(["2017", "2016", "2015", "2014"])
    .add_yaxis("二氧化硫排放量(吨)", [8753975.72, 11028643.04, 18591000, 19744000])
    .add_yaxis("氮氧化物排放量(吨)", [12588323.62, 13943109, 18510241.91, 20780015.34])
    .set_global_opts(title_opts=opts.TitleOpts(title="中国废气主要污染物排放", subtitle="SO2/氮氧化合物"))
)
    line.render("./templates/the_so2.html")
    with open("./templates/the_so2.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())
    return render_template('the_so2.html',
                           the_so2=plot_all,
                           )
if __name__ == '__main__':
  app.run(debug=True)
  
- 主要是通过.render以及with open等进行python和html档的数据交互，并且在项目中已成功实现。
```

### 部分参考链接
1. [http://pyecharts.herokuapp.com/](http://pyecharts.herokuapp.com/)
2. [https://github.com/pyecharts/pyecharts-app](https://github.com/pyecharts/pyecharts-app)
3. [https://www.jianshu.com/p/e0b2851672cd](https://www.jianshu.com/p/e0b2851672cd)
