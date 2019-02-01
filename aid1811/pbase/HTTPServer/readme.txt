httpserver v3.0
http server + 后端处理程序
功能: 
   httpserver
      获取http请求
      解析http请求
      将请求发送给webFrame
      从webFrame接收反馈数据
      将数据组织为http响应给浏览器
   webFrame(web架构):
      接收httpserver请求
      根据请求进行逻辑处理和数据处理
      将数据发送给httpserver4       
   
   升级点: 1. 采用httpserver和后端应用分离的模式,降低程序的耦合度
          2. httpserver和webFrame可以分别单独开发

   技术点: 1. httpserver和webframe通信 网络通信
          2. 封装 使用类封装
          

1.server模块
  进程并行方案分别执行不同客户端请求
  TCP流式套接字+进程
2.client模块
  发送客户端请求给后台处理模块
3.后台数据处理

*********************************************************
python的httpserver

python2 BaseHTTPServer
python3 http.server