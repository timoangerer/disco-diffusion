s3RootPath=$1
echo "Uplading to S3 path $s3RootPath"
watchDir=$2
inotifywait -r -m $watchDir -e create -e moved_to |
    while read dir action file; do
        echo "The file '$file' appeared in directory '$dir' via '$action'"
        # do something with the file
        parentDir="$(basename "$(dirname "$dir/$file")")"
        uploadPath=$s3RootPath/$parentDir
        echo "Uploading to: '$uploadPath'"
        aws s3 sync $dir $uploadPath
    done
