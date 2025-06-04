project = 'notes'
copyright = '2025, scillidan'
author = 'scillidan'
release = '0.0.1'

extensions = [
	'myst_parser',
    'sphinx_inline_tabs',
	'sphinx_copybutton',
    'sphinx_external_toc',
	'sphinxcontrib.asciinema',
    'sphinxext.photofinish',
    'sphinxcontrib.video'
]
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '.venv',
    '.gitignore',
    'README.md',
    'LICENSE-CC-BY-NC-ND'
]
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
templates_path = ['_templates']
html_static_path = ['_static']

html_title = "𝖓𝖔𝖙𝖊𝖘"
# html_additional_pages = {'index': 'your-custom-landing-page.html'}
html_sidebars = {
    "**": [
        "sidebar/scroll-start.html",
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/navigation.html",
        "sidebar/ethical-ads.html",
        "sidebar/scroll-end.html",
    ]
}
html_css_files = [
    'custom.css',
    # 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css'
]
html_theme = 'furo'
html_theme_options = {
	# "announcement": "<em>Important</em> announcement!",
    # "light_logo": "logo-light-mode.png",
    # "dark_logo": "logo-dark-mode.png",
	"sidebar_hide_name": False,
	"navigation_with_keys": False,
    "top_of_page_buttons": ["view", "edit"],
    # "light_css_variables": {
    #     "color-brand-primary": "red",
    #     "color-brand-content": "#ef6678",
    #     "color-admonition-background": "#ccbb45",
    # },
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/scillidan/notes",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
    "source_repository": "https://github.com/scillidan/notes",
    "source_branch": "main",
    "source_directory": "./"
}

external_toc_path = "_toc.yml"
external_toc_exclude_missing = False

sphinxcontrib_asciinema_defaults = {
    'theme': 'asciinema',
    'font-size': 'small',
    # 'font-family': 'Sarasa Mono SC',
    'line-height': 1.33,
    'speed': 1.5
}
sphinxext_photofinish = {
    'max_viewport_width': 800,
    'width_min': 300
}

# datatables_version = "1.13.4"
# datatables_class = "sphinx-datatable"
# datatables_options = {
#     'lengthMenu': [20, 50, 100, 200, 500],
#     'pageLength': 50,
# }