import fcntl,time,os
F='/tmp/claude-0/-home-user-nike-research-case-comp/c6360f77-8844-5e04-9011-d8ceb3c498c8/scratchpad/dt/resale_panel/.wb_last'
def wait(gap=10):
    with open(F,'a+') as f:
        fcntl.flock(f,fcntl.LOCK_EX)
        f.seek(0); s=f.read().strip()
        last=float(s) if s else 0
        d=time.time()-last
        if d<gap: time.sleep(gap-d)
        f.seek(0); f.truncate(); f.write(str(time.time())); f.flush()
        fcntl.flock(f,fcntl.LOCK_UN)
