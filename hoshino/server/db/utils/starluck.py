from tortoise.query_utils import Q
from hoshino.server.db.model.models import Starluck


async def query_star(uid: int) -> int:
    """
    :说明: `query_star`
    > 查询用户的绑定星座

    :参数:
      * `uid: int`: QQ号

    :返回:
      - `int`: 星座ID
    """
    p = await Starluck.filter(Q(uid=uid)).values("star")
    if p:
        return p[0]["star"]
    return 0


async def set_star(uid: int, star: int):
    """
    :说明: `set_user_star`
    > 绑定用户星座

    :参数:
      * `uid: int`: QQ号
      * `star: int`: 星座ID
    """
    query = Starluck.filter(Q(uid=uid))
    if await query.values("star"):
        await query.update(star=star)
    else:
        await Starluck.create(uid=uid, star=star)