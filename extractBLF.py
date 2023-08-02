import can
import cantools
import argparse

out_file = "out.csv"

parser = argparse.ArgumentParser()
parser.add_argument("-db", help="dbc can db file to import", type=str, default=False, required=False)
parser.add_argument("-blf", help="blf file to import", type=str, default="", required=True)
parser.add_argument("-csv", help="if you want a csv file, then put the csv file name here", type=str, default="", required=False)
parser.add_argument("-outfile", help="name of the output file", type=str, default="out", required=False)
parser.add_argument("-logs", help="display logs", type=str, default=False, required=False)

args = parser.parse_args()

def write_value(file, value):
    file.write(str(value))
    file.write(" : ")
  
if args.csv:
    out_file = args.outfile + ".csv"
else:
    out_file = args.outfile + ".txt"

if args.db:  
    db = cantools.database.load_file(args.db)

with open(out_file, "w+") as f:
    if args.csv:
        write_value(f, "timestamp")
    write_value(f, "id")
    if args.db: 
        write_value(f, "name")
    if args.csv:
        write_value(f, "extended")
        write_value(f, "remote_frame")
        write_value(f, "rx")
        write_value(f, "dlc")
    write_value(f, "data")
    if args.csv:
        write_value(f, "channel")
    f.write('\n')

    for msg in list(can.BLFReader(args.blf)):
        try:
            if args.logs:
                print(hex(msg.arbitration_id))
            if args.db: 
                decoded_data = db.decode_message(msg.arbitration_id, msg.data, scaling=False, allow_truncated=True)
                decoded_msg_name = db.get_message_by_frame_id(msg.arbitration_id).name
            if args.csv:
                write_value(f, msg.timestamp)
            write_value(f, hex(msg.arbitration_id))
            if args.db: 
                write_value(f, decoded_msg_name)
            if args.csv:
                write_value(f, msg.is_extended_id)
                write_value(f, msg.is_remote_frame)
                write_value(f, msg.is_rx)
                write_value(f, msg.dlc)
            if args.db: 
                write_value(f, decoded_data)
            else:
                write_value(f, msg.data)
            if args.csv:
                write_value(f, msg.channel)
            
            f.write('\n')
        except:
            print("error")
            exit()
            pass
