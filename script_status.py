import os
import sys


if
CPU_Pct=str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))

linux_filepath = "/proc/meminfo"
meminfo = dict(
    (i.split()[0].rstrip(":"), int(i.split()[1]))
    for i in open(linux_filepath).readlines()
)

meminfo["memory_total_gb"] = meminfo["MemTotal"] / (2 ** 20)
meminfo["memory_free_gb"] = meminfo["MemFree"] / (2 ** 20)
meminfo["memory_available_gb"] = meminfo["MemAvailable"] / (2 ** 20)
meminfo['persen'] = ((meminfo["memory_total_gb"] -meminfo["memory_available_gb"]) / meminfo["memory_total_gb"] *100 )

print("CPU% :{} ,Memory% :{:.2f}".format(CPU_Pct, meminfo['persen']))


if __name__ == "__main__":
    main(sys.argv)