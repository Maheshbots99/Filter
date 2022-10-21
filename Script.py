class script(object):
    START_TXT = """𝙷𝙴𝙻𝙻𝙾 {},
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 😍"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/MaHi_458>𝙼𝙰𝙷𝙴𝚂𝙷.𝚂</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: <a href=https://t.me/Ms_458>𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴</a>
✯ 𝙼𝚂.𝚄𝙿𝙳𝙰𝚃𝙴𝚂: <a href=https://t.me/Ms_458>𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴</a>
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: <a href=https://t.me/Ms_458>𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴</a>
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: <a href=https://t.me/Ms_458>𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴</a>
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>𝗡𝗢𝗧𝗘:</b>
<b>★ 𝙼𝙰𝙷𝙴𝚂𝙷.𝚂 : <a href=https://t.me/MaHi_458>𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴</a>
<b>★ 𝙼𝚂.𝚄𝙿𝙳𝙰𝚃𝙴𝚂: <a href=https://t.me/Ms_458>𝙼𝚂.𝚄𝙿𝙳𝙰𝚃𝙴𝚂</a>

<b>𝗢𝗪𝗡𝗘𝗥:</b>
<b>★ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/MaHi_458>𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴</a>"""
    MANUELFILTER_TXT = """<b>𝗛𝗲𝗹𝗽 ◕ 𝗙𝗶𝗹𝘁𝗲𝗿𝘀</b>

<b>★ Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message</b>

<b>𝗡𝗢𝗧𝗘:</b>
<b>1. 𝙼𝙰𝙷𝙴𝚂𝙷.𝚂 should have admin privillage.</b>
<b>2. only admins can add filters in a chat.</b>
<b>3. alert buttons have a limit of 64 characters.</b>

<b>𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 𝗔𝗡𝗗 𝗨𝗦𝗔𝗚𝗘:</b>
<b>• /filter - <code>add a filter in chat</b></code>
<b>• /filters - <code>list all the filters of a chat</b></code>
<b>• /del - <code>delete a specific filter in chat</b></code>
<b>• /delall - <code>delete the whole filters in a chat (chat owner only)</b></code>"""
    BUTTON_TXT = """<b>𝗛𝗲𝗹𝗽 ◕ 𝗕𝗨𝗧𝗧𝗢𝗡𝗦</b>

<b>⍟ 𝙼𝙰𝙷𝙴𝚂𝙷.𝚂 Supports both url and alert inline buttons.</b>

<b>𝗡𝗢𝗧𝗘:</b>
<b>1. Telegram will not allows you to send buttons without any content, so content is mandatory.</b>
<b>2. 𝙼𝙰𝙷𝙴𝚂𝙷.𝚂 supports buttons with any telegram media type.</b>
<b>3. Buttons should be properly parsed as markdown format</b>

<b>𝗨𝗥𝗟 ◕ 𝗕𝗨𝗧𝗧𝗢𝗡𝗦</b>
<code><b>[Button Text](buttonurl:https://t.me/Ms_458)</b></code>

<b>𝗔𝗟𝗘𝗥𝗧 ◕ 𝗕𝗨𝗧𝗧𝗢𝗡𝗦</b>
<code><b>[Button Text](buttonalert:This is an alert message)</b></code>"""
    AUTOFILTER_TXT = """<b>𝗛𝗘𝗟𝗣 ◕ 𝗔𝗨𝗧𝗢 𝗙𝗜𝗟𝗧𝗘𝗥</b>

<b>𝗡𝗢𝗧𝗘:</b>
<b>1. Make me the admin of your channel if it's private.</b>
<b>2. make sure that your channel does not contains camrips, porn and fake files.</b>
<b>3. Forward the last message to me with quotes.</b>
 <b>I'll add all the files in that channel to my db.</b>"""
    CONNECTION_TXT = """<b>𝗛𝗘𝗟𝗣 ◕ 𝗖𝗢𝗡𝗡𝗘𝗖𝗧𝗜𝗢𝗡𝗦</b>

<b>⍟ Used to connect bot to PM for managing filters</b>
<b>⍟ it helps to avoid spamming in groups.</b>

<b>𝗡𝗢𝗧𝗘:</b>
<b>1. Only admins can add a connection.</b>
<b>2. Send <code>/connect</code> for connecting me to ur PM</b>

<b>𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 𝗔𝗡𝗗 𝗨𝗦𝗔𝗚𝗘:</b>
<b>• /connect  - <code>connect a particular chat to your PM</b></code>
<b>• /disconnect  - <code>disconnect from a chat</b></code>
<b>• /connections - <code>list all your connections</b></code>"""
    EXTRAMOD_TXT = """<b>𝗛𝗘𝗟𝗣 ◕ 𝗘𝗫𝗧𝗥𝗔 𝗠𝗢𝗗𝗨𝗟𝗘𝗦</b>

<b>𝗡𝗢𝗧𝗘:</b>
<b>these are the extra features of 𝙼𝙰𝙷𝙴𝚂𝙷.𝚂</b>

<b>𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 𝗔𝗡𝗗 𝗨𝗦𝗔𝗚𝗘:</b>
<b>• /id - <code>get id of a specified user.</b></code>
<b>• /info  - <code>get information about a user.</b></code>
<b>• /imdb  - <code>get the film information from IMDb source.</b></code>
<b>• /search  - <code>get the film information from various sources.</b></code>"""
    ADMIN_TXT = """<b>𝗛𝗘𝗟𝗣 ◕ 𝗔𝗗𝗠𝗜𝗡 𝗠𝗢𝗗𝗦</b>

<b>𝗡𝗢𝗧𝗘:</b>
<b>This module only works for my admins</b>

<b>𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 𝗔𝗡𝗗 𝗨𝗦𝗔𝗚𝗘:</b>
<b>• /logs - <code>to get the rescent errors</b></code>
<b>• /stats - <code>to get status of files in db.</b></code>
<b>• /delete - <code>to delete a specific file from db.</b></code>
<b>• /users - <code>to get list of my users and ids.</b></code>
<b>• /chats - <code>to get list of the my chats and ids</b></code>
<b>• /leave  - <code>to leave from a chat.</b></code>
<b>• /disable  -  <code>do disable a chat.</b></code>
<b>• /ban  - <code>to ban a user.</b></code>
<b>• /unban  - <code>to unban a user.</b></code>
<b>• /channel - <code>to get list of total connected channels</b></code>
<b>• /broadcast - <code>to broadcast a message to all users</b></code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
M_NT_FND = """<b>This Movie Not Found My Database \n\n Request To Admin</b>"""
