import json
import sys
import queue


def main():
    config_path = "config.json"
    if sys.argv[1]:
        config_path = sys.argv[1]
    config_file = open(config_path, 'rw')
    config = json.load(config_file)
    config_file.close()

    i_queue = queue.Queue()

    gargs = config["global_args"]
    p_dict = {}
    for bot in config["bots"]:
        o_queue = queue.Queue()
        plat = bot["platform"]
        __import__(plat)
        p_dict[bot["name"]] = globals()[plat].Bot(bot, gargs, i_queue, o_queue)

    loop(iqueue, p_dict)

def loop(iqueue, p_dict):
    while True
        message = iqueue.get()

if __name__ == "__main__":
    main()
