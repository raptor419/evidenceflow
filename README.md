## **🖥️ Overview of System Architecture**

This system consists of **five web apps**, each running on a different local port on the machine 192.168.1.211. These are exposed via **Nginx or a reverse proxy** to human-friendly URLs under the domain evidenceflow.tavlab.iiitd.edu.

## **🌐 Redirection Summary**

Each internal service (running on a different port) is **mapped to a sub-path or domain** as follows:

| **Internal Address** | **App Type** | **External URL** | **Purpose** |
| --- | --- | --- | --- |
| <http://192.168.1.211:5000> | Flask app | evidenceflow.tavlab.iiitd.edu | Main backend + dashboard |
| --- | --- | --- | --- |
| <http://192.168.1.211:4000> | React app (static) | evidenceflow.tavlab.iiitd.edu/alluvial/ | Alluvial diagram visualizer |
| --- | --- | --- | --- |
| <http://192.168.1.211:3000> | React app (static) | evidenceflow.tavlab.iiitd.edu/navigator/ | Network navigation UI |
| --- | --- | --- | --- |
| <http://192.168.1.211:8000> | JS viewer (static) | evidenceflow.tavlab.iiitd.edu/sourcenetwork/ | GEXF source network visualizer |
| --- | --- | --- | --- |
| <http://192.168.1.211:6006> | TensorBoard projector | evidenceflow.tavlab.iiitd.edu/projector/ | Embedding projector visualization |
| --- | --- | --- | --- |

## **🧭 Step-by-Step Instructions**

### **0\. Connect to Remote Server**

bash

```ssh iiitd@1.1.1.211```

SSH into the server where the apps live.

### **1\. Start the Flask App (Port 5000)**

```bash

cd ~/evidenceflow/flask-dashboard-azia/

tmux

conda activate evidenceflow

python run.py
```

- Starts the **main Flask backend**.  

- Use tmux so it keeps running even after a logout.  

- Press Ctrl + b, then d to detach from the tmux session.  

### **2\. Start the Alluvial React App (Port 4000)**

```bash

cd ~/evidenceflow/alluvial-generator/build/

tmux

python -m http.server 4000
```

- Serves the **Alluvial visualization** as static content.  

Detach: Ctrl + b, then d

### **3\. Start the Network Navigator React App (Port 3000)**

```
bash

cd ~/evidenceflow/network-navigator/build/

tmux

python -m http.server 3000
```

- Launches the **network navigation interface**.  

Detach: Ctrl + b, then d

### **4\. Start GEXF Viewer (Port 8000)**

```
bash

cd ~/evidenceflow/gexf-viewer/

tmux

python -m http.server 8000
```

- Hosts **source network visualization** in GEXF format.  

Detach: Ctrl + b, then d

### **5\. Launch TensorBoard Projector (Port 6006)**

```
bash

cd ~/evidenceflow/tensor-dashboard/

tmux

conda activate evidenceflow

tensorboard --logdir embeddings/log/
```

- Serves **embedding projector** for viewing model outputs.  

Detach: Ctrl + b, then d

## **⚠️ Common Issues and Troubleshooting**

### **❌ Only Flask App is Running**

A frequent issue is that only the Flask app (port 5000) is restarted after login, while the other services (static React apps or TensorBoard) are forgotten. As a result:

- Only the main dashboard (`/`) works.  

- Pages like `/alluvial/`, `/navigator/`, `/sourcenetwork/`, and `/projector/` return 404 or connection errors.  

#### **✅ Fix:**

Manually repeat the steps above for **each webapp** using tmux to ensure they all run in parallel.

### **🔄 System Restart or Server Reboot**

When the server restarts, **all tmux sessions and running servers are lost**. None of the endpoints will work until the services are manually restarted.

#### **✅ Fix:**

After a reboot, SSH into the server and **start all 5 apps again** using the instructions above.
