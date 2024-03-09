import nextcord
from nextcord import Interaction
from nextcord.ext import commands, application_checks
from keep_alive import keep_alive
import os

TOKEN = "MTA3Nzg5MTE5MDAzMDA3Mzg5Ng.GJRcVG.9kc0E3omEdS9stFZgbDMQc4fzRnoNV_6yyWTJw"

intents = nextcord.Intents.default()
intents.message_content = True

client = commands.Bot(owner_ids = [756149983866257492, 291874601254912000], command_prefix=';', intents=intents)

watching = nextcord.ActivityType.watching
listening = nextcord.ActivityType.listening
playing = nextcord.ActivityType.playing

global x1

@client.event
async def on_ready():
    await client.change_presence(status=nextcord.Status.dnd,
                                 activity=nextcord.Activity(type=watching, name="People Die..."))
    print("Bot Online As: " + client.user.name + "#" + client.user.discriminator)

    # Reconnect
@client.event
async def on_resumed(self):
    print('Bot has reconnected!')

    # Error Handlers
@client.event
async def on_command_error(self, ctx, error):
        # Uncomment line 26 for printing debug
        # await ctx.send(error)

        # Unknown command

    if isinstance(error, commands.CommandNotFound):
            await ctx.send('Invalid Command!')

        # Bot does not have permission
    elif isinstance(error, commands.MissingPermissions):
            await ctx.send('Bot Permission Missing!')
"""@client.event
async def on_message(message):
    # channel = client.get_channel(1030698526075785298)
    # await channel.send('testing')
    print(message.author, message.content, message.channel.id)


#     pass
"""


import json
@client.event
async def on_message(message):
    if message.author.name != "Light Yagami":
      print("Message: " + message.content + " " +
          "\nAuthor: " + message.author.name)
    empty_array = []
    guild = client.get_guild(1060834133955326002)
    # guild = self.bot.get_guild(1060834133955326002)
    with open('JSON/mmroleid.json', 'r') as file:
        role_id_giver = json.load(file)
        bot_role = nextcord.utils.get(guild.roles, name="Mr. Zero")
        try:
          role_id = int(role_id_giver[str(guild.id)][0])
        except:
          print("NO ROLE AAA")
        print(role_id)
    role = nextcord.utils.get(guild.roles, name="@everyone")

    if message.author == client.user:
        return
    if str(message.channel.type) == "private":
        print(guild.channels)
        print(message.author.name)
        name = str(f"mm-{message.author.name}").lower().replace(" ", "-")
        print(name)
        x121 = str(message.author.id)
        guild1 = str(guild.id)
        test = 0
        get = nextcord.utils.get(guild.text_channels, name=name)
        with open("JSON/count.json", "r") as file:
            data = json.load(file)
            if not guild1 in data:
                with open("JSON/count.json", "r") as file:
                    data = json.load(file)
                    if not guild1 in data:
                        with open("JSON/count.json", "w") as file1:
                            data[guild1] = [test]
                            json.dump(data, file1, indent=4)
                    else:
                        with open("JSON/count.json", "w") as file1:
                            data += [guild1]
                            json.dump(data, file1, indent=4)

        if not x121 in data[guild1]:
            print("\n\n\n\n\n\n\n\nF\n\n\n\n\n\n")
            channel = nextcord.utils.get(guild.channels,
                                        name="mod-mail-log")
            create_role = await guild.create_role(
                name=f"{message.author.name.lower()}'s Mod Mail Host ")
            print(create_role)
            overwrites1 = {
                create_role:
                    nextcord.PermissionOverwrite(read_messages=True),
                role: nextcord.PermissionOverwrite(read_messages=False),
                bot_role: nextcord.PermissionOverwrite(read_messages=True)
            }
            create_channel = await guild.create_text_channel(
                f"mm-{message.author.name}", overwrites=overwrites1)
            h = await create_channel.send(
                "**Claim The Mail First by `;claim <ping client>` Then Chat With Client**"
            )
            await h.pin()
            i = await create_channel.send(
                f"**You cant Ping the client Normally! Ping The Client By Pasting This! - `<@{message.author.id}>`**"
            )
            await i.pin()
            j = await create_channel.send(
                "**If you want to Send message to the client, then first ping them then write text, ex - `@client TEXT`**"
            )
            await j.pin()
            embed777 = nextcord.Embed(
                title=
                f"There is a New Mod Mail Opened By {message.author.name}.",
                description=
                "Please Some one Claim This Mail by Typing `;claim <ping name of client>` in the  Mail Channel (Not this One, The One which has `mm` in its name!). If Anyone Goe to Help the Client Without Typing Claim Command, That wont be Good, You shall get a warning! Thank You"
            )
            await channel.send(embed=embed777)
            embed1211 = nextcord.Embed(
                title="**Thread Opened**",
                description=
                f"**Dear {message.author.mention}, Your Thread Has Been Created. A Admin or Higher Rank Will Communicate With You Soon! Please Stay tuned**"
            )
            await message.author.send(embed=embed1211)
            x = create_channel.id
            modmail_channel = client.get_channel(x)
            if message.attachments != empty_array:
                files = message.attachments
                await modmail_channel.send("[" +
                                           message.author.display_name +
                                           "]")

                for file in files:
                    await modmail_channel.send(file.url)

            else:
                embed = nextcord.Embed(
                    title="Mod Mail Message Recieved Of " +
                          message.author.display_name + " | ID - " +
                          str(message.author.id),
                    description=message.content,
                    color=0xFF0000)
                embed2 = nextcord.Embed(
                    title=
                    "Your Message is Delivered Wait For The Staff Team to reply",
                    color=0xFF0000)
                await message.author.send(embed=embed2)
                await create_channel.send(embed=embed)
            print(guild.text_channels)
            with open("JSON/count.json", "r") as file:
                data = json.load(file)
                if guild1 in data:
                    with open("JSON/count.json", "w") as file1:
                        data[guild1] += [x121]
                        json.dump(data, file1, indent=4)

        else:
            print("YEYEYE")
            x = get.id
            modmail_channel = client.get_channel(x)
            if message.attachments != empty_array:
                files = message.attachments
                await modmail_channel.send("[" +
                                           message.author.display_name +
                                           "]")

                for file in files:
                    await modmail_channel.send(file.url)
            else:
                embed = nextcord.Embed(
                    title="Mod Mail Message Recieved Of " +
                          message.author.display_name + " | ID - " +
                          str(message.author.id),
                    description=message.content,
                    color=0xFF0000)
                embed2 = nextcord.Embed(
                    title=
                    "Your Message is Delivered In {guild.name} Wait For The Staff Team to reply",
                    color=0xFF0000)
                await message.author.send(embed=embed2)
                await modmail_channel.send(embed=embed)

    elif str(message.channel).startswith(
            'mm-') and message.content.startswith('<'):
        member_object = message.mentions[0]
        if message.attachments != empty_array:
            files = message.attachments

            for file in files:
                await member_object.send(file.url)
        else:
            index = message.content.index(" ")
            string = message.content
            mod_message = string[index:]
            embed1 = nextcord.Embed(
                title=f"Staff Team Communication Services of:",
                description=mod_message,
                color=0xFF0000)
            if message.content.endswith("."):
                embed1.set_author(name=message.author.name)

                await member_object.send(embed=embed1)
            else:
                await member_object.send(embed=embed1)


xxx = []
for i in client.guilds:
    xxx += i


@client.slash_command(name="claim", description="CLAIM DA MOD MAIL", guild_ids=xxx)
@application_checks.has_permissions(kick_members = True)
async def claim(interaction : Interaction, member: nextcord.Member):
        print("IN")
        member_id = member.id
        guild = interaction.guild
        print(member)
        channel = nextcord.utils.get(guild.channels, name="mod-mail-log")
        member1 = guild.get_member(int(member_id))
        print("IN2")
        print(member1.name.lower())
        main_role = nextcord.utils.get(guild.roles, name=f"{member1.name.lower()}'s Mod Mail Host")
        print(member1.name.lower())
        print(main_role)
        print(main_role)
        await interaction.user.add_roles(main_role, reason=None, atomic=True)
        try:
          mm_channel = nextcord.utils.get(guild.channels, name=f"mm-{member1.name.lower()}")
        except:
          print("Mod Mail Not Found")
          return
        embed = nextcord.Embed(title=f"***{interaction.user.name} Claimed {member1.display_name}'s Mod Mail! DMed Ganime About this Claim! If Anyone Else Interfere The Person Who Claimed the Mod Mail, The Person will Get a certain kick by The Superiror Staff***", color=0xFF0000)
        embed1 = nextcord.Embed(title=f"***Your Mod Mail Has Been Claimed, The Claimer Will Contact You Soon***", color=0xFF0000)
        print("PASS BABE")
        await channel.send(embed=embed)
        await member1.send(embed=embed1)
        await interaction.response.send_message("MAIL CLAIMED!")


@client.slash_command(name="remove-mod-mail", description="REMOVE DA MAIL", guild_ids=xxx)
@application_checks.has_permissions(manage_guild = True, administrator = True)
async def mm_remove(interaction : Interaction, member: nextcord.Member):
      print("IN")
      guild = interaction.guild
      channel = nextcord.utils.get(guild.channels, name="mod-mail-log")
      main_role = nextcord.utils.get(guild.roles, name=f"{member.name.lower()}'s Mod Mail Host")
      print(member.name.lower())
      print(main_role)
      await main_role.delete()
      guild_id = str(guild.id)
      with open("JSON/count.json", "r") as file:
        print("IN")
        data = json.load(file)
        print("IN")
        x = str(member.id)
        print("IN")
        print(x)
        y = data[guild_id].index(x)
        print("BRUH")
        if guild_id in data:
          print("BRA")
          with open("JSON/count.json", "w") as file1:
            print("IN")
            del data[guild_id][y]
            print("IN")
            json.dump(data, file1, indent=4)
        print("IN")
        embed = nextcord.Embed(title="Your Thread Has Been Closed! If You want To Start The Thread Again, Just Send Me a DM! Note - If you dont reply to the Message of Staff within 24 Hours, The Thread May get Closed")
        embed2 = nextcord.Embed(title=f"{interaction.user.name} Has Closed the Ticket of {member.name}!")
        await channel.send(embed=embed2)
        await member.send(embed=embed)
        await interaction.channel.delete(reason=None)
        print("OUT")



@client.slash_command(name="set-mod-mail-role", description="SET DA ROLE", guild_ids=xxx)
@application_checks.has_permissions(manage_channels= True)
async def set_mm_role(interaction : Interaction, role_id : str):
      guild_id = interaction.guild_id
      channel_id = int(role_id)
      print("YES")
      with open('JSON/mmroleid.json', 'r') as file:
            welcome_data = json.load(file)
            welcome_guild = str(guild_id)
            print(welcome_guild)
            print(channel_id)

            # Update existing ticket
            if welcome_guild in welcome_data:
                welcome_data[welcome_guild] += [channel_id]
                with open('JSON/mmroleid.json', 'w') as update_ticket_data:
                    json.dump(welcome_data, update_ticket_data, indent=4)

            # Add new ticket
            else:
                print("IN")
                welcome_data[welcome_guild] = [channel_id]
                print("IN2")
                with open('JSON/mmroleid.json', 'w') as new_ticket_data:
                    print("IN3")
                    json.dump(welcome_data, new_ticket_data, indent=4)
                    print("IN4")
      print("IN5")
      color = nextcord.Colour.red()
      role = interaction.guild.get_role(channel_id)
      embed2 = nextcord.Embed(title=f"The Role {role.name}, has been assigned as the Mod Mail Role", color=color)
      await interaction.response.send_message(embed=embed2)

@client.slash_command(name="clear", description="KILL MESSAGES HAHAHAHA", guild_ids=xxx)
async def clear(interaction : Interaction, amt : str):
    amt = int(amt)
    await interaction.channelmrge(amt)
    await interaction.response.send_message(f"{amt} messages deleted")
    await interaction.message.delete()
@client.slash_command(name="inf_msg", description=" HAHAHAH", guild_ids=xxx)
@application_checks.is_owner()
async def inf_msg(interaction : Interaction, member: nextcord.Member, num : str, msg : str):
    await interaction.response.send_message(f"Sent the Message - '{msg}' to {member.name} {num} times!")
    num = int(num)
    for i in range(num):
        await member.send(f"{member.mention} " + msg)


@client.slash_command(name="say", description="REPEAT HAHAHAH", guild_ids=xxx)
async def say(interaction : Interaction, words : str):
    print("RUN")
    await interaction.response.send_message(words)
    #channel1 = ctx.channel
    #channel = client.get_channel(921289830124642327)
    #await channel1.send(f'hello there {ctx.author.mention}')

@client.slash_command(name="whoisl", description="Asking a PERSONAL Question...", guild_ids=xxx)
async def whoisl(interaction : Interaction):
    print("RUN")
    await interaction.response.send_message("So... L was my good friend who died due to the kira Case... ("
                                            "Or I killed Him Because He was out smartting me and I am a Dirty Killer?)")
#await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))
choices1 = ["Watching", "Listening", "Playing"]

@client.slash_command(name="set_activity", description="change my work (Only My Creators Can Do This)", guild_ids=xxx)
@application_checks.is_owner()
async def set_activity(interaction:Interaction, work : str, category:str=nextcord.SlashOption(name="type", description="type of activity",choices=choices1)):
    if category == "Watching" :
        await client.change_presence(status= nextcord.Status.dnd, activity=nextcord.Activity(type=watching, name=work))
    if category == "Playing" :
        await client.change_presence(status= nextcord.Status.dnd, activity=nextcord.Activity(type=playing, name=work))
    if category == "Listening" :
        await client.change_presence(status= nextcord.Status.dnd, activity=nextcord.Activity(type=listening, name=work))

    await interaction.response.send_message("Activity Type Set To " + category)

@client.slash_command(name="laugh", description="hehehehehehheeee", guild_ids=xxx)
async def laugh(interaction: Interaction):
    print("RUN")
    await interaction.response.send_message("Sooda... BOKU NO KIRA DA...Ha..HAHA...HAHAHAHAHAAA...HAAHAHAHAHAHAHHA"
                                            "AA....HAAAAAAAAAAAAAAAAAHAHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA..ARGH..AGHH"                                              "ARGH..AHHAA.**&^*&^$%%.....(chokes because of laughter)... ok that"
                                            "...that was enough...but anyways, NOW AFTER L's DEATH I AM GOD OF THE"
                                            "NEW WORLD HAHAHAHAHA *lights theme plays*")

keep_alive()
try:
    client.run(TOKEN)
except nextcord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    os.system("python restarter.py")
    os.system('kill 1')