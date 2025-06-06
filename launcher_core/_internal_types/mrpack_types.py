# This file is part of async-mc-launcher-core (https://github.com/JaydenChao101/async-mc-launcher-core)
# SPDX-FileCopyrightText: Copyright (c) 2025 JaydenChao101 <jaydenchao@proton.me> and contributors
# SPDX-License-Identifier: BSD-2-Clause
from typing import TypedDict, Literal


class MrpackFileHashes(TypedDict):
    sha1: str
    sha256: str


class MrpackFileEnv(TypedDict):
    client: Literal["required", "optional", "unsupported"]
    server: Literal["required", "optional", "unsupported"]


class MrpackFile(TypedDict, total=False):
    path: str
    hashes: MrpackFileHashes
    env: MrpackFileEnv
    downloads: list[str]
    fileSize: int


MrpackDependencies = TypedDict(
    "MrpackDependencies",
    {"minecraft": str, "forge": str, "fabric-loader": str, "quilt-loader": str},
    total=False,
)


class MrpackIndex(TypedDict, total=False):
    formatVersion: int
    game: str
    versionId: str
    name: str
    summary: str
    files: list[MrpackFile]
    dependencies: MrpackDependencies
