names = [name.strip() for name in open("names.txt", "r")]
distinct_names=set(names)
for distinct_name in distinct_names:
    print(distinct_name, names.count(distinct_name))


directories = ["/".join(directory.split("/")[2:-1]) for directory in open("images_directory.txt", "r")]
distinct_directories = set(directories)
for distinct_directory in distinct_directories:
    print("{0} -> {1}\n".format(distinct_directory,directories.count(distinct_directory)))