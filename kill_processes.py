import psutil

def find_processes_by_port(port):
    matching_pids = set()

    for conn in psutil.net_connections(kind="inet"):
        if conn.laddr.port == port and conn.status == psutil.CONN_LISTEN:
            if conn.pid and conn.pid != 0:
                matching_pids.add(conn.pid)

    return list(matching_pids)

def kill_processes(pids):
    for pid in pids:
        try:
            proc = psutil.Process(pid)
            print(f"🔧 Terminating PID {pid} ({proc.name()})...")
            proc.terminate()
            proc.wait(timeout=3)
            print(f"✅ Killed PID {pid}")
        except Exception as e:
            print(f"❌ Failed to kill PID {pid}: {e}")

def main():
    ports = [8000, 9999]
    all_pids = set()

    for port in ports:
        pids = find_processes_by_port(port)
        if pids:
            print(f"🔍 Found listening PIDs on port {port}: {', '.join(map(str, pids))}")
            all_pids.update(pids)
        else:
            print(f"✅ No listening processes found on port {port}")

    if all_pids:
        kill_processes(all_pids)
    else:
        print("✅ No processes to kill.")

if __name__ == "__main__":
    main()
