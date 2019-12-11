# pytest Documentation阅读

## 阅读目标
1. 掌握pytest的设计理念, 能编写测试插件, 组织测试框架
2. 完整的搞定一个国外优秀库的文档阅读, 从而为其他优秀的代码库文档阅读提供信息和经验
3. 找1个使用pytest做测试的优秀开源库, 看他是如何写测试用例的: 比如异步web框架: starlette, 既是异步, 又有99%的代码覆盖率


## 阅读周期
2019年9月末-2019年1月末, 共4个月

## 复习
monkey-patch的使用(pytest原生固件):
pip install pytest-ordering

"""All modifications will be undone after the requesting
    test function or fixture has finished.(fixture finish也是指所在scope包含的case跑完tear down后再undone)"""
    
test_monkeypatch.py
  
  
功能更强大的pytest-mock的使用:
pip install pytest-mock


pytest插件探索——hook开发, 个人感觉还是要看一下testng的listener
https://segmentfault.com/a/1190000018623872

## chapter2 
pytest --maxfail=2 # stop after two failures
pytest --pdb:  在出错的case处会进入pdb调试模式

Disabling plugins: 例如
pytest -p no:randomly

pytest --pastebin=all: 把结果输出到bpaste.net


## chapter4
Assertion Rewriting
pytes支持在失败的assert语句的子表达式中显示中间值, 用的是这个技术,
但是它只会显示test用例中的assertion的中间值, 对依赖的模块要显示值, 可以在conftest中注册一下: register_assert_rewrite

## chapter5

### fixture
pytest --fixtures test_simplefactory.py 显示所有可用的fixture

fixture本质上是一种依赖注入, test function是fixture的消费者
conftest.py则可以用来存放共享的fixtures
sharing test data:
    1. 在fixture中load data, 然后把该fixture给多个测试用例使用. 起到缓存数据的作用
    2. 使用tests folder, 插件如pytest-datadir, pytest-datafiles, 目前已经实验了前一个: test_hello.py

### Scope
scope="module": 同一个模块中的test function都会使用同一个fixture, 节省时间

## 编写插件
https://pluggy.readthedocs.io/en/latest/#pluggy pytest是基于pluggy构建的, 因此理解pluggy对理解plugin有帮助
https://segmentfault.com/a/1190000018623872: plugin中文文档
https://docs.pytest.org/en/2.8.7/writing_plugins.html#writing-plugins
https://docs.pytest.org/en/2.8.7/_modules/_pytest/hookspec.html
一个plugin的官方例子: https://docs.pytest.org/en/latest/example/nonpython.html#yaml-plugin done


所有插件都要以pytest_开头


### writing hook functions
略

我仔细查看了几个pytest的文档, 理解了pytest的编写原理, 使用pluggy来驱动代码运行, 事实上pytest本身也是pluggy来驱动的

这个回答总结了pytest的运行过程, 可以结合_pytest/runner.py来看
https://stackoverflow.com/questions/38667429/pytest-plugin-overriding-pytest-runtest-call-and-friends/38823263#38823263

hookspec在这个文件定义: Lib/site-packages/_pytest/hookspec.py
运行过程在这个文件定义:  Lib/site-packages/_pytest/runner.py

大致流程如下, 没有指明路径的, 都在_pytest/runner.py里:

```
_pytest/main.pytest_collection
_pytest/main.pytest_runtestloop
    loop pytest_runtest_protocol(不同的用例)
        pytest_runtest_logstart
        runtestprotocol
            call_and_report('setup')
            call_and_report('call')
                call_runtest_hook
                    CallInfo.from_call
                        pytest_runtest_call(item: Function)
                            _pytest/python.py.Function.runtest
                                _pytest/python.py.pytest_pyfunc_call
                                    # 就里运行真正的测试用例
                                    testfunction(**testargs)
                pytest_runtest_makereport
                pytest_runtest_logreport
                pytest_exception_interact
            call_and_report('teardown')
        pytest_runtest_logfinish
```










