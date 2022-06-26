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
                            

                            @help.command ()
async def memes(ctx):
    embed=discord.Embed(title="IndianDesiMemer Help Center ✨", description="Commands of **meme** \n`yar meme     :` Complet Dsei Memes",inline=False)
    embed.set_footer(icon_url=ctx.author.avatar_url,text="Command requested by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)
                            
                            
                            
                            
                            
