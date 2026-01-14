from handle import handler
from config import WS_HOST, WS_PORT

import asyncio
import websockets

# 群消息服务
async def main():
    ws1 = await websockets.serve(handler, WS_HOST, WS_PORT)
    print(f"正在监听 {WS_HOST}:{WS_PORT}")
    await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("程序已停止")