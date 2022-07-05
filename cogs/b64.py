from discord.ext import commands
import base64

class b64(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('b64 Online')

    @commands.command()
    async def b64(self, ctx, action, string):
        # "encode" or "e" entered
        if action == "encode" or action == "e":
            string = string.encode('ascii')
            b64_bytes = base64.b64encode(string)
            output = b64_bytes.decode('ascii')
            await ctx.send(output)
            return [output, True]

        # "decode" or "d" entered
        elif action == "decode" or "d":
            string = string.encode('ascii')
            b64_bytes = base64.b64decode(string)
            output = b64_bytes.decode('ascii')
            await ctx.send(output)
            return [output, True]

            # # HELP MENU
            # embed = discord.Embed(title="__base64 Command Menu__", color=0x2b2a2a)
            # embed.add_field(value="**decode** or **d** - decode base64 encoded text", inline=False)
            # embed.add_field(value="**encode** or **e** - base64 encode text", inline=False)
            # await ctx.send(embed=embed)

def setup(client):
    client.add_cog(b64(client))