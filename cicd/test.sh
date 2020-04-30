
#!/usr/bin/env bash
echo "Running CICD tests"
cd $1
if python3 test.py; then
    echo "Tests suceeded"
else
    git checkout HEAD~1
fi
