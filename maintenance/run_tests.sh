su -m vagrant <<'EOF'
  source maintenance/env.sh
  utilitiespackage system version
  utilitiespackage system selftest
  utilitiespackage system selfcoverage
EOF
