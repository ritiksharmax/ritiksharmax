# 🚀 GitHub Profile Setup Instructions

Follow these quick steps to make this profile live on your GitHub account:

---

### Step 1: Create Your Profile Repository on GitHub
1. Go to [GitHub - New Repository](https://github.com/new).
2. Set the **Repository name** to match your exact GitHub username (e.g., `ritiksharmax` or your handle).
   > GitHub will show a special banner: *"✨ You found a secret! `ritiksharmax/ritiksharmax` is a special repository that you can use to add a README.md to your GitHub profile."*
3. Make sure the repository is set to **Public**.
4. Check **"Add a README file"** (or leave it unchecked if you are pushing directly from local).

---

### Step 2: Push These Files to Your Profile Repository

Run the following commands in your terminal:

```bash
cd /Users/ritiksharma/.gemini/antigravity-ide/scratch/github-profile

# Initialize git if needed
git init
git branch -M main

# Add all profile files & automated snake workflow
git add .
git commit -m "feat: setup high-tech dark neon ML engineer profile"

# Link to your profile repository (replace with your actual github url)
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/<YOUR_GITHUB_USERNAME>.git

# Push to main
git push -u origin main
```

---

### Step 3: Enable the Automated Contribution Snake Workflow
1. In your profile repository on GitHub, navigate to the **Actions** tab.
2. If prompted, click **"I understand my workflows, go ahead and enable them"**.
3. Under **Workflows** on the left sidebar, click **"Generate Contribution Snake Animation"**.
4. Click **Run workflow** -> **Run workflow** (green button).
5. In your repository settings:
   - Go to **Settings** > **Actions** > **General**.
   - Scroll down to **Workflow permissions**.
   - Select **Read and write permissions** and click **Save**.
   - Run the workflow again if needed.

---

### Step 4: Customize Your Details
You can edit [README.md](./README.md) anytime to update:
- Your LinkedIn / Hugging Face / X handles
- Project links and descriptions
- Research interests or new technologies
