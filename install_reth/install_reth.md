# Install reth-lighthouse

### 1. Install reth

```bash
VERSION=v0.1.0-alpha.1
curl -LO https://github.com/paradigmxyz/reth/releases/download/$VERSION/reth-$VERSION-x86_64-unknown-linux-gnu.tar.gz
tar -xvf reth-$VERSION-x86_64-unknown-linux-gnu.tar.gz
sudo mv reth /usr/bin/
```

### 2. Make jwtsecret

```bash
openssl rand -hex 32 | tr -d "\n" | sudo tee /home/ubuntu/work/jwtsecret
sudo chmod 644 /home/ubuntu/work/jwtsecret
```

### 3. Setup reth

`vim /lib/systemd/system/reth.service`

```bash
[Unit]

Description=Reth Full Node
After=network-online.target
Wants=network-online.target

[Service]

WorkingDirectory=/home/ubuntu/work
User=ubuntu
Environment=RUST_LOG=info
ExecStart=RUST_LOG=info reth node --authrpc.jwtsecret /home/ubuntu/work/jwtsecret --authrpc.addr 127.0.0.1 --authrpc.port 8551 --http --http.api "eth,net,web3,txpool" --http.corsdomain "*" --ws --ws.port 8556 --ws.addr "0.0.0.0" --ws.api eth,net,web3 --ws.origins '*'
Restart=always
RestartSec=5s

[Install]
WantedBy=multi-user.target
```

### 4. Enable and start reth

```bash
sudo systemctl enable reth
sudo systemctl start reth
```

### 5. Install lighthouse

```bash
VERSION=v4.2.0
wget https://github.com/sigp/lighthouse/releases/download/$VERSION/lighthouse-$VERSION-x86_64-unknown-linux-gnu.tar.gz
tar zxvf lighthouse-$VERSION-x86_64-unknown-linux-gnu.tar.gz
sudo mv lighthouse /usr/local/bin/
```

`※ Chú ý:` Cần thay đổi lighthouse về cái mới nhất. Tìm trên trang này

https://github.com/sigp/lighthouse/releases

 

### 6. Setup lighthouse

`vim /lib/systemd/system/lighthouse.service`

```bash
[Unit]

Description=Lighthouse consensus client
After=network-online.target
Wants=network-online.target

[Service]

WorkingDirectory=/home/ubuntu
User=ubuntu
Environment=RUST_LOG=info
ExecStart=/usr/local/bin/lighthouse --datadir /home/ubuntu/.lighthouse/mainnet bn --network mainnet --execution-endpoint http://localhost:8551 --http-address 0.0.0.0 --http --execution-jwt /home/ubuntu/work/jwtsecret --builder http://localhost:18550 --checkpoint-sync-url https://mainnet.checkpoint.sigp.io --metrics --disable-deposit-contract-sync
Restart=always
RestartSec=5s

[Install]
WantedBy=multi-user.target
```

### 7. Enable and start lighthouse

```bash
sudo systemctl enable lighthouse
sudo systemctl start lighthouse
```
