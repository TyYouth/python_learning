"""
内容参考:segmentfault@betacat:Python中的异常处理
"""

# except 和 finally 都不是必须, 但是必须有其中一个
# 如果有需要, 使用finally来释放资源
# 如果有需要, 请不要忘记在处理异常后做清理工作或者回滚操作
# except 可以有多个, 也可以用元组形式同时指定多个异常
# except (TypeError, ValueError) as e:
import sys


def Div(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Error: Denominator(b) should not be zero")
    except (TypeError, ValueError) as e:
        print("Unexpected Error: {}".format(e))
    except:
        # get detial from sys.exc_info method
        error_type, error_value, trace_back = sys.exc_info()
        print(error_value)
        raise
    else:
        print("Run into else only when everythin goes well")
    finally:
        print("anyway, always run into Finally block")


Div(2, 0)
Div(2, "unsupported operand type(s)")
Div(2, 1)
