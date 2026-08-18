# immich-tools

Use `requirements.txt` to install necessary modules.

```bash
pip install -r requirements.txt
```

## Help

```bash
Usage: immich-tools [OPTIONS] COMMAND [ARGS]...

  This is immich-tools version 0.2.24

Options:
  -d, --debug          Enable debug mode
  -l, --log-path TEXT  path to directory where logs will be stored, works only
                       if --log-file flag is set to True
  --help               Show this message and exit.

Commands:
  assign-album-tags       looking in album for specified tags and return...
  change-owner-photo      change ownership of all assets in the album to...
  check-album-tags        looking in album for specified tags and return...
  merge-xmp               Merge xmp sidecards to original image file from...
  refresh-album-metadata  Refresh metada in all assets in album
  run-job                 Runs job, possible values: thumbnailGeneration,...
  version                 shows version
```
### Commands
#### Assign album tags
```bash
Usage: immich-tools assign-album-tags [OPTIONS] ALBUM_ID

  looking in album for specified tags and return assets without expected tags.
  Use all as album id to assign tags in all albums

Options:
  -k, --api-key TEXT  [required]
  -u, --url TEXT      [required]
  -c, --create-tag    will create missing tags if needed
  --help              Show this message and exit.
```

#### Change owner of the photo
```bash
Usage: immich-tools change-owner-photo [OPTIONS] ALBUM_ID

  change ownership of all assets in the album to you. Use all as album id to
  change ownership of all albums

Options:
  -k, --api-key TEXT  [required]
  -u, --url TEXT      [required]
  --help              Show this message and exit.
```

#### check album tags
```bash
Usage: immich-tools check-album-tags [OPTIONS] ALBUM_ID

  looking in album for specified tags and return assets without expected tags

Options:
  -k, --api-key TEXT  [required]
  -u, --url TEXT      [required]
  -t, --tag TEXT      expected tags (use multiple -t/--tag)  [required]
  -a, --add-missing   will add missing tags
  -c, --create-tag    will create missing tags if needed
  --help              Show this message and exit.
```

#### Merge xmp sidecards to original image file

```bash
  Merge xmp sidecards to original image file from PATH recursively

Options:
  -x, --leave-xmp       use to leave xmp files and do not remove them
  -o, --leave-original  will create copy of original file with '_original'
                        suffix
  --dry-run             will run without modifying or removing any file
  --help                Show this message and exit.
```

#### Refresh metadata in all assets in album

```bash
Usage: immich-tools refresh-album-metadata [OPTIONS] ALBUM_ID

  Refresh metada in all assets in album

Options:
  -k, --api-key TEXT  [required]
  -u, --url TEXT      [required]
  --help              Show this message and exit.
```

#### Run job

```bash
Usage: immich-tools run-job [OPTIONS] JOB_NAME

  Runs job, possible values: thumbnailGeneration, metadataExtraction,
  videoConversion, faceDetection, facialRecognition, smartSearch,
  duplicateDetection, backgroundTask, storageTemplateMigration, migration,
  search, sidecar, library, notifications, backupDatabase

Options:
  -k, --api-key TEXT  [required]
  -u, --url TEXT      [required]
  --help              Show this message and exit.
```

