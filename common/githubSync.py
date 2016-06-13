import commands

def main(path_str):
	cmd = "cd %s && git pull -q --all -p" % (path_str)
	stat_t = commands.getstatusoutput(cmd)
	return stat_t
