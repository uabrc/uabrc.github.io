---
date: 2026-08-12T09:00:00-05:00
categories:
    - Known Issues
---

# MATLAB Issues

There is a critical, hard-to-diagnose MATLAB parpool bug in versions before R2022a.

The issue arises when using a `parpool` for multiple jobs simultaneously, as with an `sbatch --array` job. MATLAB `parpool` can be started manually, or at the first `parfor` loop encountered, among other functionality. See the [MATLAB Documentation](https://www.mathworks.com/help/parallel-computing/run-code-on-parallel-pools.html) for more information and a complete list.

<!-- more -->

Before R2022a, MATLAB assumed that only one parpool will be used at a time for each user, and put necessary communication files in a common directory. When multiple parpools are run simultaneously by the same user, they may attempt to write to those files at the same time, corrupting the files, resulting in a range of obscure Parallel Computing Toolbox (PCT) errors. The collisions are effectively random, which can make the issue hard to reproduce and hard to diagnose. The more parpools open simultaneously, the more likely there will be at least one error. In the worst case, we have seen unrecoverable corruption of the parpool common directory, which can be fixed by deleting the directory.

Symptoms of the bug include:

- Excessive load and context switching on affected nodes
- Inconsistent and varied PCT errors
- Inability to start Matlab parpool

To avoid the bug, please use the latest available version of MATLAB and no earlier than R2022a. Upgrading MATLAB versions may require some effort and testing of your code, because MATLAB is not always backwards compatible. Be sure to test that your code works as expected on the new version before using it for research.

If you aren't able to use R2022a or newer, there is a workaround available. Please navigate to this [GitHub repository](https://github.com/wwarriner/matlab_parpool_slurm_fix) and follow the instructions in `README.md`. Some light MATLAB programming is required to effectively use the workaround. Please contact [Support](../../../../help/support.md) if you would like assistance.
