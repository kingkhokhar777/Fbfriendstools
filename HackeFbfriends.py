import marshal,zlib,base64
exec(zlib.decompress(base64.b64decode("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