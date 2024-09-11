# Tutorial on Usage of Parallelization-based Software in Cheaha

## Sequential Execution

Breaking a bigger problem into set of tasks, and executing these tasks one by one on a single CPU.

## Parallel Execution

Divide a larger problem into a series of smaller tasks and execute these tasks using multiple CPUs. The application should leverage parallelization technology to utilize multicore processors, multiple nodes, multiple GPUs, or a hybrid approach (such as combining CPUs and GPUs).

## Types of Parallelization

### Shared Memory Parallelization

In this method, your job executes independent tasks on separate cores within the same compute node. These tasks share the node's resources and communicate by reading from and writing to shared memory.

For instance, OpenMP is a parallel directive that supports shared memory parallelization.

### Distributed Memory Parallelization

Tasks can be distributed on different compute nodes and executed. The tasks communicate each other using message passing. A widely used standard to achieve this kind of parallelism is Message Passing Interface (MPI).

## A Sampling of Parallel Software

### Gromacs

Gromacs is specifically meant for high-performance molecular dynamics and analysis.

Recent Gromacs version available in Cheaha can be loaded as,

```bash
$module load rc/GROMACS/2022.3-gpu
```

Some of the simulation examples are covered in the [Gromacs Tutorial Page](http://www.mdtutorials.com/gmx/).We will take the example of Lysozyme in water as a case study.

Download and extract the example `pdb` dataset using the following command,

```bash
$DATA_SET=water_GMX50_bare
$wget -c https://ftp.gromacs.org/pub/benchmarks/${DATA_SET}.tar.gz
$tar xf ${DATA_SET}.tar.gz
```

To run the simulation using `gmx` executable,

```bash
$cd ./water-cut1.0_GMX50_bare/1536
$gmx grompp -f pme.mdp
$gmx mdrun -ntmpi 4 -nb gpu -pin on -nsteps 5000 -ntomp 10 -s topol.tpr
```

In the above run command,

- `gmx` is the executable to run the pipeline.
- `-ntmpi` Number of MPI processes.
- `-nb gpu`defines the computation to use GPUs.
- `-pin on` binds CPU to core.
- `-nsteps 5000` Number of steps to run the simulation.
-`-ntomp 10` Number of cores, which will be 10*4 MPI processes i.e, 40 cores
- `-s topol.tpr` is the input parameter.

#### Performance Analysis

### Quantum Espresso

Quantum Espresso (QE) is an open-source suite of codes for electronic-structure calculations and materials modeling based on density functional theory (DFT), plane waves, and pseudopotentials. It is used to study the properties of materials at the atomic scale.

Quantum Expresso is available as a module in Cheaha and can be loaded as,

```bash
$module load QuantumESPRESSO/6.3-foss-2018b
```
