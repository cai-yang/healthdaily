#-*-coding:utf-8-*-
import redis
from rq import Worker, Queue, Connection

# 你需要先创建一个 Redis，然后将 Redis 的 URL 替换到下面
conn = redis.from_url('redis://:Cyaiqki7UpqV2xWBgNb8VcpQtM99tuwnOKoGvYIkVfwGRh8owpMBtys8ob2apmam@boqyovqrmlxy.redis.sae.sina.com.cn:10093')

listen = ['high', 'default', 'low']

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
