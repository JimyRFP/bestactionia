module.exports = {
  apps: [
    {
      name: "bestactionia",
      script: "./.venv/bin/uvicorn",
      args: "main:app --port 8761",
      interpreter: "./.venv/bin/python3",
      watch: false
    }
  ]
}
