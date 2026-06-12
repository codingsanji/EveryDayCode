def compare_instagram_lists(followers_file, following_file):
    try:
        # Read the files
        with open(followers_file, 'r', encoding='utf-8') as f:
            # We filter for lines that look like usernames (no spaces, non-empty)
            followers = set(line.strip() for line in f if line.strip() and " " not in line.strip())
            
        with open(following_file, 'r', encoding='utf-8') as f:
            following = set(line.strip() for line in f if line.strip() and " " not in line.strip())

        # Logic: Who are you following that isn't in your followers list?
        unfollowers = following - followers
        
        # Logic: Who follows you that you don't follow back? (Fans)
        fans = followers - following

        print(f"--- Statistics ---")
        print(f"Followers count: {len(followers)}")
        print(f"Following count: {len(following)}")
        print(f"------------------\n")

        print(f"Users NOT following you back ({len(unfollowers)}):")
        for user in sorted(unfollowers):
            print(f"[-] {user}")

        print(f"\nUsers you don't follow back ({len(fans)}):")
        for user in sorted(fans):
            print(f"[+] {user}")

    except FileNotFoundError as e:
        print(f"Error: Could not find file {e.filename}. Make sure it's in the same folder.")

if __name__ == "__main__":
    # Just point these to your text files
    compare_instagram_lists('followers.txt', 'following.txt')
