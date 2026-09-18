@echo off
echo ==============================================
echo   Syncing LeetCode / DSA to GitHub...
echo ==============================================

git add .
git commit -m "feat(dsa): auto-sync daily leetcode solutions [%date% %time%]"
git push origin main

echo.
echo ==============================================
echo   Sync complete! Check your GitHub heatmap!
echo ==============================================
timeout /t 3
