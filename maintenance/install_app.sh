su -m vagrant <<'EOF'
  source maintenance/env.sh
  cd utilities
  pip install .
EOF
