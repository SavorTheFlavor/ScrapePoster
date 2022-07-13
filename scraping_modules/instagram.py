import instaloader
import config

profiles = []

insta = instaloader.Instaloader()
insta.login(config.IG_USER, config.IG_PASSWORD)

# Getting the list of accounts from usernames
for profile in config.IG_ACCOUNTS:
    try:
        profiles.append(instaloader.Profile.from_username(insta.context, profile))
        print(profiles)
    except:
        print(f'User "{profile}" does not exist.')
