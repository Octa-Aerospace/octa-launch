## Notes to setup a router/wifi connection with a device


1. **Make the runner script executable**

```bash
chmod +x runner.sh
```

2. **Run the script with sudo permissions**

```bash
sudo bash runner.sh
```

3. **That should install the NetworkManager package and open up the GUI for you to connect to a network.**

<img width="792" alt="Screenshot 2025-01-06 at 12 26 12 AM" src="https://github.com/user-attachments/assets/c0b79e2c-90d8-4ae4-9e8b-0ba7f48c0bf8" />

4. **Select the network you want to connect to and enter the password.**

5. **In the "Edit a Connection" dialog, you must set your desired network in the topmost field.**

This way, the network will be connected to automatically when the device is in range; It's important that you set the network as the topmost one in the list.

<img width="792" alt="Screenshot 2025-01-06 at 12 26 58 AM" src="https://github.com/user-attachments/assets/250c657d-3b79-41f6-8207-ccbf035713b7" />

6. **Then just go "Back" and you should be connected to the network.**

That's it! 🚀

Now your raspberry pi will try to connect to the network automatically as soon as it loads up.
