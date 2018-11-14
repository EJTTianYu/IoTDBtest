#coding=utf-8

UPDATE="/Users/tianyu/PycharmProjects/generateTest/UPDATE.txt"

def writeUPDATE():
    with open(UPDATE,"w") as fin:
        #新建存储组用于UPDATE测试
        #fin.write("SET STORAGE GROUP TO root.updateTest;\n")
        #测试不同的时间序列
        fin.write("CREATE TIMESERIES root.updateTest.d0.s16 WITH DATATYPE=TEXT, ENCODING=PLAIN;\n")
        #每种类型插入999条数据用于测试
        for num in range(1,1000):
            num1=str(num)
            fin.write('insert into root.updateTest.d0(timestamp,s16) values('+num1+','+'\'EX\''+');\n')


if __name__=="__main__":
    writeUPDATE()