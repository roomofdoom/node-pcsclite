{
	"targets": [
		{
			"target_name": "pcsclite",
			"sources": [
				"src/addon.cpp",
				"src/pcsclite.cpp",
				"src/cardreader.cpp"
			],
			"cflags": [
				"-Wall",
				"-Wextra",
				"-Wno-unused-parameter",
				"-fPIC",
				"-fno-strict-aliasing",
				"-fno-exceptions",
				"-pedantic"
			],
			"conditions": [
				[
				"OS=='linux'",
				{

				}],[
					"OS=='mac'",
					{
						"libraries": [
							"-framework",
							"PCSC"
						],
						"include_dirs": [
							"<!(node -e \"require('nan')\")"
						]
					}
				],
				[
					"OS=='win'",
					{
						"libraries": [
							"-lWinSCard"
						],
						"include_dirs": [
							"<!(node -e \"require('nan')\")"
						]
					}
				]
			]
		}
	]
}
