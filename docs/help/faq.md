# Frequently Asked Questions (FAQ)

## Common Issues

### Why do I get an error when I try to launch an HPC Interactive session?

If you are seeing an error like the following when launching an HPC Interactive job, please read on for the most likely solution.

![!HPC Interactive error dialog.](images/faq_ood_hpc_interactive_conda_init_error.png)

The most common cause is that the command `conda init` was used, creating a block in your `.bashrc` file that looks like the following section. [Anaconda](../cheaha/conda.md) is managed as a [module](../cheaha/lmod.md), so it is not necessary to use `conda init`. To avoid the issue reoccurring, please do not use `conda init`.

```bash
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/<YOUR_USER>/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/<YOUR_USER>/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/home/<YOUR_USER>/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/<YOUR_USER>/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```

To locate your `.bashrc` file, please navigate to `https://rc.uab.edu`, login and click the `Files` dropdown in the top navigation menu. Click "Home Directory". More detailed instructions on the file browser can be found at [OOD Files](/docs/cheaha/open_ondemand/ood_files.md).

Once you've opened the file browser, check the checkbox labeled "Show Dotfiles" in the top-right of the page, then find the file `.bashrc` in the file browser pane and select it.

![!Home files list with Show Dotfiles check and .bashrc highlighted.](images/faq_ood_file_browser_bashrc.png)

Click the "Edit" button. In the new tab that opens, delete the section shown above and click "Save".

![!Edit tab with highlighted section.](images/faq_ood_editor_conda_init.png)

Please try to launch your job again. If it still doesn't work, please [contact us](/docs/index.md#contact-us)
