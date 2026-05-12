# GitHub Setup Guide - Push Your Code

## Step 1: Create GitHub Account (5 minutes)

1. Go to: https://github.com
2. Click "Sign up"
3. Enter email, password, username
4. Verify email
5. ✅ You now have a GitHub account!

---

## Step 2: Install Git (5 minutes)

**On Windows:**

1. Download: https://git-scm.com/download/win
2. Run installer
3. Click "Next" for all defaults
4. **Important:** Choose "Use Git from the Windows Command Prompt"
5. Finish installation

**Verify Git installed:**
```powershell
git --version
```
Should show: `git version 2.xxx.x`

---

## Step 3: Configure Git with Your Name & Email (2 minutes)

Open PowerShell and run:

```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@gmail.com"
```

**Example:**
```powershell
git config --global user.name "Alex Kumar"
git config --global user.email "alex@gmail.com"
```

Verify it worked:
```powershell
git config --global user.name
git config --global user.email
```

---

## Step 4: Create GitHub Repository (2 minutes)

1. Go to https://github.com/new
2. Fill in:
   - **Repository name:** `pbc-platform-engineer`
   - **Description:** `Platform Engineer Learning Journey - AWS, Python, Kubernetes`
   - **Public** (so you can show it to employers!)
3. ✅ Click "Create repository"

You'll see a page with setup instructions. **Copy the HTTPS URL** (looks like: `https://github.com/YOUR-USERNAME/pbc-platform-engineer.git`)

---

## Step 5: Push Your Local Code to GitHub (5 minutes)

Open PowerShell in your project folder:

```powershell
cd C:\Users\DELL\Desktop\Pthon for Devops

# Initialize Git repository
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: Platform engineer learning materials"

# Add GitHub repository as remote
git remote add origin https://github.com/YOUR-USERNAME/pbc-platform-engineer.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Replace `YOUR-USERNAME` with your actual GitHub username!**

---

## Step 6: Verify Push Succeeded ✅

1. Go to https://github.com/YOUR-USERNAME/pbc-platform-engineer
2. You should see all your files!
3. ✅ Success!

---

## Complete Commands (Copy & Paste)

```powershell
# Go to your project folder
cd "C:\Users\DELL\Desktop\Pthon for Devops"

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Python basics, AWS, Terraform, Docker, Kubernetes learning materials"

# Add remote (REPLACE YOUR-USERNAME!)
git remote add origin https://github.com/YOUR-USERNAME/pbc-platform-engineer.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## Troubleshooting

### Problem: "Authentication failed"
**Solution:** GitHub now requires Personal Access Token instead of password

1. Go to https://github.com/settings/tokens
2. Click "Generate new token"
3. Select scopes: repo, workflow
4. Copy the token
5. When prompted for password in PowerShell, paste the token

### Problem: "fatal: not a git repository"
**Solution:** Run `git init` first in your folder

### Problem: "error: refspec main does not match any"
**Solution:** Run: `git branch -M main` before pushing

### Problem: "remote already exists"
**Solution:** Your remote is already configured (it's fine!)

---

## Workflow After First Push

For future updates:

```powershell
# After making changes:
git add .
git commit -m "Your message here"
git push
```

That's it! No need for origin/branch stuff after first push.

---

## Example Commits

Good commit messages:

```
git commit -m "Add Week 1 Python syntax exercises"
git commit -m "Add Week 2 control flow examples"
git commit -m "Add boto3 AWS automation script"
git commit -m "Fix: handle file not found error"
git commit -m "Update README with setup instructions"
```

---

## Your GitHub URL

After setup, your repository will be at:

```
https://github.com/YOUR-USERNAME/pbc-platform-engineer
```

**Share this with:**
- Your portfolio
- Resume
- Employers
- Interviewers

---

## Next: After First Push ✅

1. Go to your GitHub repository
2. Click ⭐ to star it (bookmark for yourself)
3. Check if all your files are there
4. You're ready to add more code!

---

**Need help? Message me when you:**
- ✅ Have GitHub account created
- ✅ Have Git installed
- ✅ First push is complete
- ✅ Can see code on GitHub.com

You got this! 🚀
