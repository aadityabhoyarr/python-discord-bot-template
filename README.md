# Python-Discord-Bot-Template

This repository is a Python Discord bot template that anyone can use to start building their own Discord bot. It is specially designed for beginner programmers who are just starting to learn how to work with `discord.py.` Please keep in mind that while this template may not be the absolute best one available, it is still a great starting point for learning how Discord bots work and for creating your own bot with ease.

## Index
* [💪- Support](#--support)
* [🎫-Get the Discord Token](#-get-the-discord-token)
* [✉️-Invite Your Bot to Join a Server](#%EF%B8%8F-invite-your-bot-to-join-a-server)
* [📩-How to download it](#-how-to-download-it)
* [🚦-How to start](#-how-to-start)
* [👩‍💻-Code in detail](#-code-in-detail)
* [📖-Library Used](#-library-used)

## 💪- Support 

- Please ensure that you keep the credits and a link to this repository in all files containing my code. This will help me as a developer, and new programmers can access the link to get some additional help if needed
- If you are unfamiliar with the basics of discord.py, [here](https://www.pythondiscord.com/resources) is a link to some resources that can help you learn.

## 🎫-Get the Discord Token

Here are the step to creating a Discord Bot account:
- Make sure you’re logged on to the [Discord website.](https://discord.com/) 
- Navigate to the [application page.](https://discord.com/developers/applications)
- Click on the “New Application” button.

<img src = "https://github.com/aadityabhoyar/python-discord-bot-template/blob/main/media/107.jpg">


- Give the application a name and click “Create”.

<img src =  "hhttps://github.com/aadityabhoyar/python-discord-bot-template/blob/main/media/108.jpg">

- Go to the “Bot” tab and click “Add Bot”. Confirm by clicking "Yes, do it!"

<img src =  "https://github.com/aadityabhoyar/python-discord-bot-template/blob/main/media/110.jpg">

 **Keep the default settings for Public Bot (checked) and Require **OAuth2 Code Grant**(unchecked).**
- `Your bot has been created.`

<img src =  "https://github.com/aadityabhoyar/python-discord-bot-template/blob/main/media/111.jpg">

- Copy the token. Remember, this token is your bot's password, so don't share it with anyone. Sharing it could allow someone to log in to your bot and perform malicious actions. If the token accidentally gets shared, you can regenerate it.

## ✉️-Invite Your Bot to Join a Server

Now you have to get your Bot User into a server. To do this, you should create an invite URL for it.
- Go to the "OAuth2" tab. Then select "bot" under the "scopes" section.

<img src =  "https://github.com/aadityabhoyar/python-discord-bot-template/blob/main/media/image-123.jpg">

- Now choose the permissions you want for the bot. Our bot is going to mainly use text messages so we don't need a lot of the permissions. You may need more depending on what you want your bot to do. Be careful with the "Administrator" permission.

<img src =  "https://github.com/aadityabhoyar/python-discord-bot-template/blob/main/media/image-124.jpg">

- After selecting the appropriate permissions, click the 'copy' button above the permissions. That will copy a URL which can be used to add the bot to a server.Paste the URL into your browser, choose a server to invite the bot to, and click “Authorize”.
- Now that you've created the bot user, we'll start writing the Python code for the bot.

## 📩-How to download it

- Clone/Download the repository by typing the following command in your terminal (Linux, Mac & Windows), or your Command Prompt ( Windows) .
- `if u get an error like: 'git' is not recognized as an internal or external command, u need to download Git.` 
- [For more help visit](https://stackoverflow.com/questions/4492979/git-is-not-recognized-as-an-internal-or-external-command)

```
git clone https://github.com/MrAdityaBhoyar/Python-Discord-Bot-Template.git
```
- Or just download the repo

## 🚦-How to start
- Before getting started u need to download the library `discord.py`, by typing the following command in your terminal (Linux, Mac & Windows), or your Command Prompt ( Windows) .

```
pip install -r requirements.txt
```
- Now fill the important information in [main.py](https://github.com/MrAdityaBhoyar/Python-Discord-Bot-Template/blob/main/main.py)

| Variable                  | What it is                                                            |
| ------------------------- | ----------------------------------------------------------------------|
| YOUR_BOT_PREFIX_HERE      | The prefix you want to use for normal commands                        |
| YOUR_BOT_TOKEN_HERE       | The token of your bot                                                 | 


## 👩‍💻-Code in detail

About the code in detail
### on_ready
```
@client.event
async def on_ready():
    print("We have logged in as {0.user} ".format(client)) 
    activity = discord.Game(name=".help", type=3)               
    await client.change_presence(status=discord.Status.online, activity=activity)
```
This command will print we have logged in as botname, and this is for making the status as an online and writing prefix in playing a game

<img src =  "https://github.com/aadityabhoyar/python-discord-bot-template/blob/main/media/112.jpg">

### Help Command
```
@client.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(title="IndianDesiMemer Help Center ✨",color=0xF49726)
    embed.add_field(name="Command Categories :",value="🐸 `memes    :` Image generation with a memey twist.\n" + "🔧 `utility  :` Bot utility zone\n😏 `nsfw     :` Image generation with a memey twist.\n\nTo view the commands of a category, send `.help <category>`" ,inline=False)
    embed.set_footer(icon_url=ctx.author.avatar_url,text="Help requested by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)
```
this command will print the help command and you can customise it as your need

<img src =  "https://github.com/aadityabhoyar/python-discord-bot-template/blob/main/media/113.jpg">

### Sub-help command

```
#Sub-help command of memes
@help.command ()
async def memes(ctx):
    embed=discord.Embed(title="IndianDesiMemer Help Center ✨", description="Commands of **meme** \n`.meme:`Memes",inline=False)
    embed.set_footer(icon_url=ctx.author.avatar_url,text="Command requested by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)
                            

#Sub-help commands of nsfw                           
@help.command ()
async def nsfw(ctx) :
    embed=discord.Embed(title="IndianDesiMemer Help Center ✨", description="Commands of **nsfw** \n`.nsfw:`NSFW", color=0xF49726)
    embed.set_footer(icon_url=ctx.author.avatar_url,text="Command requested by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)


#Sub-help commands of utility                           
@help.command ()
async def utility(ctx) :
    embed=discord.Embed(title="IndianDesiMemer Help Center ✨", description="Commands of **utility** \n`.ping:`Latency", color=0xF49726)
    embed.set_footer(icon_url=ctx.author.avatar_url,text="Command requested by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)
```

Like:

<img src =  "https://github.com/aadityabhoyar/python-discord-bot-template/blob/main/media/114.jpg">

### Cooldown

```
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("**Try after {0} second ".format(round(error.retry_after, 2)))    
        
@client.command()
@commands.cooldown(1, 10, commands.BucketType.channel) # 1 Command every 10 sec                           
async def meme(ctx):
    await ctx.send("Memes")        
```
Cooldown is used to prevent the bot from spam attack,its basically in your own need

<img src =  "https://github.com/aadityabhoyar/python-discord-bot-template/blob/main/media/115.jpg">

### NSFW

```
@client.command()
@commands.cooldown(1, 10, commands.BucketType.channel)
async def nsfw(ctx):
  if ctx.channel.is_nsfw():
     print("nsfw work!!")
  else:
    print("You can use this command in a nsfw channel only !")         
```
Many bot creators may want to add an NSFW command to their bots, but it is crucial to ensure that users are protected and that the content expires safely. To achieve this, the command should only be executed in an age-restricted channel.

<img src =  "https://cdn.discordapp.com/attachments/1054093794414444544/1054093896050819182/116.jpg">

## 📖-Library Used 
- [discord.py](https://pypi.org/project/discord.py/)
- [requests](https://pypi.org/project/requests/)
