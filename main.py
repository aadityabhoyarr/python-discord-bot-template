import discord
from discord.ext import commands


token = YOUR_BOT_PREFIX_HERE
prefix = YOUR_BOT_TOKEN_HERE

client = commands.Bot(command_prefix= prefix)
client.remove_command("help") #to remove the default boring help command


@client.event
async def on_ready():
    print("We have logged in as {0.user} ".format(client)) 
    activity = discord.Game(name=".help", type=3                # this is to writing prefix in playing a game.(optional)
    await client.change_presence(status=discord.Status.online,  # this is for making the status as an online and writing prefix in playing a game.(optional)  
                                 activity=activity)
                            
                            
                            
#Help commands
@client.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(title="IndianDesiMemer Help Center ✨",color=0xF49726)
    embed.add_field(name="Command Categories :",value="🐸 `memes    :` Image generation with a memey twist.\n" + "🔧 `utility  :` Bot utility zone\n\n" ,inline=False)
    embed.set_footer(icon_url=ctx.author.avatar_url,text="Help requested by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)
                            

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


# it is used for the cooldown to prevent the bot from spam attack                             
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("**Try after {0} second ".format(round(error.retry_after, 2)))                            
                            
                            
#meme command                            
@client.command()
async def meme(ctx):
    
    response = requests.get("https://meme-api.herokuapp.com/gimme/"+"memes"+"memes"+"?t=all?hot")
    
    m = response.json()
    postLink = (m["postLink"])
    subreddit = (m["subreddit"])
    title = (m["title"])
    imageUrl =  (m["url"])
    upVote = (m["ups"])
    uv = str(upVote)

    embed=discord.Embed(title= title, url=postLink,color=0xF49726)
    embed.set_image(url=imageUrl)
    embed.set_footer(text="\n👍\t"+ uv+ "  By :r/"+subreddit)
    await ctx.send(embed=embed)                            
                            

#ping command                            
@client.command()
async def ping(ctx):
    await ctx.send('Ping! **{0}**ms'.format(round(client.latency, 1)))
    
                            
                            
                            
