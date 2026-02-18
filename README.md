<h2 align="center">
  𝑱𝒂𝒑𝒂𝒏𝒆𝒔𝒆 𝑿 𝑹𝒂𝒏𝒌𝒊𝒏𝒈
</h2>

<p align="center">
  <img src="https://github.com/TeamJapanese/Japanese-X-Ranking/blob/main/img/ranking.png" width="700"/>
</p>

<p align="center">
<b>
ᴀ ʀᴇᴀʟ-ᴛɪᴍᴇ ᴛʏᴘɪɴɢ ᴄᴏᴍᴘᴇᴛɪᴛɪᴏɴ ᴇɴɢɪɴᴇ  •  
ʙᴜɪʟᴛ ꜰᴏʀ ʜɪɢʜ-ᴘᴇʀꜰᴏʀᴍᴀɴᴄᴇ ɢʀᴏᴜᴘs  •  
ᴅᴇꜱɪɢɴᴇᴅ ꜰᴏʀ ꜱᴄᴀʟᴇ  •  
ꜰᴀɪʀ ʙʏ ᴀʀᴄʜɪᴛᴇᴄᴛᴜʀᴇ  •  
ʀᴇᴀᴅʏ ꜰᴏʀ ʀᴇᴀʟ-ᴡᴏʀʟᴅ ᴘʀᴏᴅᴜᴄᴛɪᴏɴ
</b>
</p><p align="center">
<a href="https://github.com/TeamJapanese/Japanese-X-Ranking/stargazers"><img src="https://img.shields.io/github/stars/TeamJapanese/Japanese-X-Ranking?color=black&logo=github&logoColor=black&style=for-the-badge" alt="Stars"/></a>
<a href="https://github.com/TeamJapanese/Japanese-X-Ranking/network/members"><img src="https://img.shields.io/github/forks/TeamJapanese/Japanese-X-Ranking?color=black&logo=github&logoColor=black&style=for-the-badge"/></a>
<a href="https://github.com/TeamJapanese/Japanese-X-Ranking/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blueviolet?style=for-the-badge" alt="License"/></a>
<a href="https://github.com/TeamJapanese/Japanese-X-Ranking/commits/main"><img src="https://img.shields.io/github/last-commit/TeamJapanese/Japanese-X-Ranking?color=black&logo=github&logoColor=black&style=for-the-badge" /></a>
<a href="https://www.python.org/">
  <img src="https://img.shields.io/badge/Written%20in-Python-blue?style=for-the-badge&logo=python" alt="Python"/>
</a>
</p>


---



## What is Japanese X Ranking?

**Japanese X Ranking** is far more than a typical Telegram competition bot.
It is a production-grade real-time typing challenge engine designed for automation, fairness, and long-term scalability

Engineered and maintained by **[ᴛᴇᴧᴍ ᴊᴧᴘᴧɴᴇsᴇ](https://github.com/TeamJapanese)** this project follows a clear philosophy:

A public implementation is available on Telegram as
**[𝑱𝒂𝒑𝒂𝒏𝒆𝒔𝒆 𝑿 𝑹𝒂𝒏𝒌𝒊𝒏𝒈](http://telegram.dog/JapaneseXRankbot?start=true)**

Whether you manage a small private group or a large public community, Japanese X Ranking provides a stable and competitive ecosystem built for serious engagement.

---

## Why this project exists

Most Telegram game bots were created for fun — not for performance or reliability.

Common problems include:

- Manual round control
- Weak ranking recalculation logic
- Spam-based reward abuse
- Inconsistent database structure
- Fake or manipulated leaderboards
- Poor scalability in large groups

These limitations make them unsuitable for long-term competitive communities.


---

## Team Japanese approach

**Japanese X Ranking** was designed from the architecture level to solve these issues.

This project:

- Runs fully automated timed challenge loops
- Uses MongoDB-backed persistent ranking storage
- Locks winners instantly to prevent duplicate rewards
- Calculates points and coins with strict validation
- Implements expiration timers for each round
- Separates ranking logic from messaging layer
- Ensures fair-play through structured validation

This is not a demo bot.
It is a structured competition engine built for longevity.

Built by **[sᴧɴᴅᴇᴇᴘ sʜᴧʀᴍᴧ](https://github.com/itzsandeepshrma)** **for developers**, with production reality in mind.


---

## Core Capabilities

- Real-time typing challenges in Telegram groups
- First-correct-answer instant win system
- Automated points & coins distribution
- Global Top 10 leaderboard system
- Personal ranking & stats tracking
- Win streak reward multiplier
- Daily bonus reward logic
- Rank tiers (Beginner → Elite → Legend)
- Fully automated 24/7 execution
- Low-latency async performance
- Anti-spam & anti-cheat safeguards

---


### Deployment Options

<p align="center"> <a href="https://render.com"><img src="https://img.shields.io/badge/Render-white?style=for-the-badge&logo=render&logoColor=black" /></a> <a href="#"><img src="https://img.shields.io/badge/Linux-VPS-black?style=for-the-badge&logo=linux" /></a> </p>


### Deploy on Render 

**Japanese X Ranking** is fully optimized for **Render**, providing a clean, stable, and production-grade deployment experience.  
Render handles infrastructure, restarts, and scaling automatically, allowing you to focus purely on development.

This method is recommended for:
- Long-running Telegram bots
- Stable uptime with automatic restarts
- Clean logs and monitoring
- Hassle-free production deployment

Follow the steps below carefully to deploy without issues.

## Render Deployment (Recommended)

<p align="center">
  <a href="https://render.com">
    <img src="https://img.shields.io/badge/Deploy%20on%20Render-white?style=for-the-badge&logo=render&logoColor=black" />
  </a>
</p> 



.### Step 1 Create a New or Existing Account on Render

1. Fork this **[Repository](https://github.com/TeamJapanese/Japanese-X-Ranking/fork)**
2. Go to **[Render](https://render.com)**
3. Create A **[New Account](https://dashboard.render.com/register)** or Use **[Existing Account](https://dashboard.render.com/login)**
4. Create a **New Web Service**
5. Connect your GitHub repository

### Step 2 Repository Configuration

1. Choose Your Forked **[Repository](https://github.com/TeamJapanese/Japanese-X-Ranking/fork)**
2. Select **Branch** main
3. Select **Root Directory** Optional (If you want to add root)
4. Select **Build Command** ```$ pip install -r requirements.txt```
5. Select **Command** ```$ python3 -m Japanese```

### Step 3 Environment Variables

1. Go to **Environment** **[Add Environment Variables](https://github.com/TeamJapanese/Japanese-X-Ranking/blob/main/.env.sample)** and add the following:
2. Make sure all values are correct and Incorrect or missing variables will cause the service to fail.

### Step 4 Deploy

- Click **Create Web Service**
- Render will install dependencies and start the bot automatically
- Wait until the status shows **Live**

### Step 5 Bot Access

- Once deployed successfully, your bot will be live on **[Telegram](
http://telegram.dog/JapaneseXRankbot?start=true)**


### Note

- No database is required for basic usage
- Logs can be monitored directly from the Render dashboard
- Free tier may sleep on inactivity; paid plans are recommended for production use
- Render deployment provides a clean, scalable, and maintenance-free environment suitable for production workloads.

---

## VPS / Local Deployment (Manual Setup)

<p align="center"> <a href="#"><img src="https://img.shields.io/badge/Linux-VPS-black?style=for-the-badge&logo=linux" /></a> </p>

If you prefer **full control**, you can deploy Japanese X Ranking on your **VPS** or **local machine**.  
This method gives **maximum stability, customizability, and 24/7 uptime**.

---

## VPS/ Local Host Deployment Steps :

Update and upgrade your server:
```bash
sudo apt-get update && sudo apt-get upgrade -y

### Install Python3 and pip

sudo apt-get install python3 python3-pip -y
sudo pip3 install --upgrade pip setuptools

### Optional: Install tmux to run the bot in the background:

sudo apt install tmux -y

### Clone the Repository

git clone https://github.com/TeamJapanese/Japanese-X-Ranking
cd Japanese-X-Ranking

### Install Dependencies

pip3 install -r requirements.txt

### Configure Environment Variables

### For Normal Windwos VPS/Local Deployment

API_ID=
API_HASH=
BOT_TOKEN=
MONGO_URL=

## For Linux Deployment

export API_ID=
export API_HASH=
export BOT_TOKEN=
export MONGO_URL=
export ENV=

### Run the Bot

python3 -m Japanese

### Optional : Run with tmux (keep running after logout)

tmux
python3 -m Japanese
# Press Ctrl+b then d to detach

### To reattach:

tmux attach
```



### Note

- Ensure Python version is compatible (3.10+ recommended)
- VPS gives full uptime, unlike free dynos on Heroku
- Secure your server (firewall, SSH keys, etc.)
- MongoDB Atlas or local MongoDB can be used

### When to Use VPS / Local

- Full-time 24/7 uptime
- Production-ready deployment
- Maximum control and customizability
- Large-scale userbots or advanced Telegram services


## Support & Updates

Stay connected with **[ᴛᴇᴧᴍ ᴊᴧᴘᴧɴᴇsᴇ](https://github.com/TeamJapanese)** for help, updates, and announcements.  

- **Channel :-** **[Team Japanese](https://t.me/TeamJapaneseOfficial)** 
- **Supporrt :-** **[Team Japanese Support](https://t.me/TeamJapaneseSupport)**

## License 

**MIT License**

**Copyright (c) 2026** **[TeamJapanese](https://github.com/TeamJapanese)**

**Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:**

**The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.**

**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.**


---



