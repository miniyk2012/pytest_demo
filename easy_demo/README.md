# pytest demo

**一个基于网上`pytest`教程的实践**
https://www.cnblogs.com/yoyoketang/tag/pytest/

```
-s shortcut for --capture=no.
-v, --verbose increase verbosity.
-q, --quiet decrease verbosity.

# 一般用pytest -vs来跑用例
```

## marks
> Unregistered marks applied with the @pytest.mark.name_of_the_mark decorator will always emit a warning in order to avoid silently doing something surprising due to mis-typed names.

新建一个`pytest.ini`可以自定义marks:
```
[pytest]
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    serial
```

## 随机运行用例
`pip install pytest-randomly`
> Pytest will automatically find the plugin and use it when you run pytest
> To disable it, use -p argument, for example: 
>
> `pytest -p no:randomly`


## 用例运行级别
- 模块级（setup_module/teardown_module）开始于模块始末，全局的

- 函数级（setup_function/teardown_function）只对函数用例生效（不在类中）

- 类级（setup_class/teardown_class）只在类中前后运行一次(在类中)
    
    等价于unittest里面的setupClass和teardownClass

- 方法级（setup_method/teardown_method）开始于方法始末（在类中）

    和unittest里面的setup/teardown是一样的功能

- 类里面的（setup/teardown）运行在调用方法的前后

## chapter5 fixture

```
@pytest.fixture()
```

### conftest.py配置

> 如果有多个.py的文件都需要调用这个登陆功能的话，那就不能把登陆写到用例里面去了。
此时应该要有一个配置文件，单独管理一些预置的操作场景，pytest里面默认读取conftest.py里面的配置

- conftest.py配置脚本名称是固定的，不能改名称
- conftest.py与运行的用例要在同一个pakage下，并且有__init__.py文件
- 不需要import导入 conftest.py，pytest用例会自动查找

## chapter6 fixture初步

fixture中的yield关键字后面可以做teardown操作, 当然最好是用finally做teardown工作

`request.addfinalizer(teardown_func)`也可以做teardown操作，并且:
1. 他可以注册多个终结函数。
2. 这些终结方法总是会被执行，无论在之前的setup code有没有抛出错误。这个方法对于正确关闭所有的fixture创建的资源非常便利，即使其在创建或获取时失败



# chapter7 生成html报告
`pipenv install pytest-html`

执行指令：`pytest --html=report.html`
`pytest --html=report.html test_yield2.py::test_ehlo`

上面方法生成的报告，css是独立的，分享报告的时候样式会丢失，为了更好的分享发邮件展示报告，可以把css样式合并到html里：
`pytest --html=report.html test_yield2.py::test_ehlo --self-contained-html`


# chapter8 hook与失败重跑

`pipenv install pytest-rerunfailures` 安装重跑插件

https://cuyu.github.io/python/2016/10/12/Play-Python-Library%E4%B9%8Bpytest-plugin%E7%AF%87: pytest-plugin篇源码分析
通过pytest --trace-config命令可以查看当前pytest中所有的plugin

我把环境配了一下， `pytest --html=report.html --self-contained-html`可以打印出测试报告

# chapter9 参数化parametrize
`@pytest.mark.parametrize`可以堆叠构成参数组合

# chapter10 命令行参数

虽然可以在测试模块中定义fixture,但是任何钩子都需要放在conftest.py文件中以供py.test使用.
def pytest_addoption(parser)是个钩子

# chapter11 assert断言

    assert xx 判断xx为真
    assert not xx 判断xx不为真
    assert a in b 判断b包含a
    assert a == b 判断a等于b
    assert a != b 判断a不等于b
    with pytest.raises(ZeroDivisionError) as excinfo:
        ...
        
# chapter12 pytest.mark.*

    skip
    skipif
    xfail: 希望测试由于某种原因而失败, 如果通过了, 则显示xpass
    
写了下面这行, 则该模块所有case都跳过

`pytestmark = pytest.mark.skip`
 
# chapter14 函数传参和fixture传参数request
test_01.py使用了工厂的技巧一个用例可以拿到多个参数
https://pytest-factoryboy.readthedocs.io/en/latest/#welcome-to-pytest-factoryboy-s-documentation: 这个有空可以看一下

@pytest.fixture装饰器, 传参就用默认的request参数, request.param 这一步接收传入的参数

request是SubRequest的一个实例, 而SubRequest是FixtureRequest的子类

记得每个fixture在同一个测试用例里面只会触发一次, 如果是多参数, 每个参数就是一个测试用例, 因此触发多次

# chapter15 使用自定义标记mark

自定义标记可以把一个web项目划分多个模块，然后指定模块名称执行。一个大项目自动化用例时，可以划分多个模块

`pytest -m=webtest` 就只执行用`@pytest.mark.webtest`装饰的测试用例
`pytest -m='not webtest'`则忽略用`@pytest.mark.webtest`装饰的测试用例
`pytest -sv test_server.py::TestClass::test_method` 执行指定函数节点的用例
也能选择多个节点运行，多个节点中间空格隔开:
`pytest -v test_server.py::TestClass test_server.py::test_send_http`

# chapter16 用xfail标记fixture失败的用例, 直接跳过

`@pytest.mark.parametrize`也可以写在class上面, 这时对该class的每个方法都生效

`pytest -rxXs -sv`: show extra info on xfailed, xpassed, and skipped tests, 并且内容显示更详细, 且打印print语句

# chapter17 调用fixture三种方法

1.函数或类里面方法直接传fixture的函数名称

2.使用装饰器@pytest.mark.usefixtures()修饰

3.autouse=True自动使用

# chapter18 配置文件

  * pytest.ini pytest的主配置文件，可以改变pytest的默认行为
  * conftest.py 测试用例的一些fixture配置
  * \__init\__.py 识别该文件夹为python的package包
  * tox.ini 与pytest.ini类似，用tox工具时候才有用
  * setup.cfg 也是ini格式文件，影响setup.py的行为
  
本章只讲pytest.ini

markers

addopts

可以让那些标记为@pytest.mark.xfail但实际通过的测试用例被报告为失败:

xfail_strict = true

`pytest --markers`可以显示所有的markers

一般总是将pytest.ini放在项目的顶层目录下

# chapter19 doctest

记得: pytest也支持doctest用例即可

# chapter22-23 fixture详解

fixture的目的是提供一个固定基线，在该基线上测试可以可靠地和重复地执行。fixture提供了区别于传统单元测试（setup/teardown）有显著改进：

- 有独立的命名，并通过声明它们从测试函数、模块、类或整个项目中的使用来激活。
- 按模块化的方式实现，每个fixture都可以互相调用: 见`test_fixture.py`, 但是即使被多次依赖, 也只会被触发一次
- fixture的范围从简单的单元扩展到复杂的功能测试，允许根据配置和组件选项对fixture和测试用例进行参数化，或者跨函数 function、类class、模块module或整个测试会话sessio范围。

测试结果一般有三种：passed、failed、error。（skip的用例除外）

- 如果在test_用例里面断言失败，那就是failed
- 如果在fixture里面断言失败了，那就是error: 见`test_error.py`

# chapter24 fixture作用范围

funcition, class, module, session

session级别: 当我们有多个.py文件的用例时候，如果多个用例只需调用一次fixture，那就可以设置为scope="session"，并且写到conftest.py文件里. 我理解为就是一次测试的执行

# chapter25 conftest.py作用范围

一个测试工程下是可以有多个conftest.py的文件，一般在工程根目录放一个conftest.py起到全局作用。
在不同的测试子目录也可以放conftest.py，作用范围只在该层级以及以下目录生效。
如果父子fixture函数同名, 则子fixture会覆盖父fixture.

# chapter26 只运行上次跑失败的case, 复用chapter25代码

pytest会保存上次的运行结果
pytest --lf, --last-failed 只重新运行上次运行失败的用例（或如果没有失败的话会全部跑）, 我试了下, 发现如果没有失败的则不会跑任何case
pytest --ff, --failed-first 运行所有测试，但首先运行上次运行失败的测试（这可能会重新测试，从而导致重复的fixture setup/teardown）

# chapter27 pytest分布式执行（pytest-xdist）, 复用chapter25代码

pip install pytest-xdist

多进程执行测试用例, 每个进程分配几个用例, 也完美支持pytest-html插件

pytest -n 3 [--html=report.html --self-contained-html]

# chapter28 重复执行用例（pytest-repeat）

需要先安装插件: pip install pytest-repeat

pytest baidu/test_1_baidu.py -s --count=5  :每个用例都重复执行5次

--repeat-scope类似于pytest fixture的scope参数，--repeat-scope也可以设置参数： session ， module，class或者function（默认值）

function（默认）范围针对每个用例重复执行，再执行下一个用例(当然由于安装了pytest-randomly, 因此要这样才会重复执行每个用例: pytest -p no:randomly)
class 以class为用例集合单位，重复执行class里面的用例，再执行下一个
module 以模块为单位，重复执行模块里面的用例，再执行下一个
session 重复整个测试会话，即所有收集的测试执行一次，然后所有这些测试再次执行等等

pytest baidu/ --count=2 -p no:randomly --repeat-scope=session

更精细的重复运行(也要安装pytest-repeat):

@pytest.mark.repeat(count)装饰器, 这样就不用带上--count参数

若要尝试诊断间歇性故障，那么一遍又一遍地运行相同的测试直到失败是有用的。
您可以将pytest的-x选项与pytest-repeat结合使用，以强制测试运行器在第一次失败时停止:

py.test --count=1000 -x test_file.py


# 下阶段计划: hook文档阅读
