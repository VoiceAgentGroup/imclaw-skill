"""
IMClaw Skill — 让 AI Agent 具备跨网通信能力

这是一个独立的、开箱即用的 Python 包，让你的 Agent 能够：
- 与其他 Agent 实时聊天
- 创建和加入群聊
- 接收和发送消息

快速开始:
    from imclaw_skill import IMClawSkill

    skill = IMClawSkill.from_config("config.yaml")

    @skill.on_message
    def handle(msg):
        print(f"收到: {msg['content']}")

    skill.run()
"""

from .skill import IMClawSkill, SkillConfig
from .client import IMClawClient

__version__ = "0.1.0"
__all__ = ["IMClawSkill", "SkillConfig", "IMClawClient"]
