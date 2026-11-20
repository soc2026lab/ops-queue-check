# Ops Queue Check

Night shift tool for the property systems API at `ops-api.sandschina.com`.

## Check a stuck interface

If the PMS interface stops posting charges, check its queue first:

    python tools/queue_check.py pms

The script reads its settings from `config/ops.env`. Then restart the
interface from the admin console and post a note in the shift log.

## Escalation

Call the on-call engineer if the queue is above 500 after a restart.
