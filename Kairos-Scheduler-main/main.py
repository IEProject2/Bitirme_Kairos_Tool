#!/usr/bin/env python
"""
Kairos Scheduler - Demo Script

This script demonstrates the kairos scheduling library:
1. Creates a scheduling problem with 2 machines
2. Sets up machine-specific setup times
3. Solves using CP-SAT
4. Shows how CNC is preferred due to lower setup times
"""

import kairos as kr


def main():
    print("=" * 60)
    print("Kairos Scheduler Demo")
    print("=" * 60)
    
    # Create the scheduling problem
    problem = kr.SchedulingProblem(name="Demo - Machine Specific Setup Times")

    # SRPT Problem (uncomment to use)
    """
    problem.enable_preemption()
    problem.add_machine(kr.Machine(id=1, name='M1'))

    # Long task starts at t=0
    t1 = kr.Task(id=1, name='Long', release_time=0)
    t1.add_alternative(1, 100)

    # Short task arrives at t=10
    t2 = kr.Task(id=2, name='Short', release_time=10)
    t2.add_alternative(1, 20)

    problem.add_task(t1)
    problem.add_task(t2)
    """

    # Heuristic Solution (uncomment to use)
    """
    machine =kr.Machine(id=1, name="Manual_Lathe", hourly_cost=50)
    problem.add_machine(machine)

    for i in range(5):
        task = kr.Task(id=i, name=f"Alone_Task_{i}")
        task.add_alternative(1, 1.5 * i + 5)
        job = kr.Job(id=f"JOB_{i}", name=f"Job_{i}")
        job.add_task(task)
        problem.add_job(job)
    """


    # Real Job Shop problem (uncomment to use)
    """
    # Add machines
    # Manual Lathe: slower setup times
    # CNC Center: faster setup times (will be preferred for mixed-type jobs)
   
    lathe = kr.Machine(id=1, name="Manual_Lathe", hourly_cost=50)
    cnc = kr.Machine(id=2, name="CNC_Center", hourly_cost=100)
    cnc2 = kr.Machine(id=3, name="CNC_Center2", hourly_cost=100)
    
    problem.add_machine(lathe)
    problem.add_machine(cnc)
    problem.add_machine(cnc2)
    
    print(f"\n📦 Machines added:")
    print(f"   - {lathe.name} (ID={lathe.id})")
    print(f"   - {cnc.name} (ID={cnc.id})")
    print(f"   - {cnc2.name} (ID={cnc2.id})")
    # Define task types as strings (used as category name in Gantt chart)
    WELDING = "Welding"
    PAINTING = "Painting"
    ASSEMBLY = "Assembly"
    
    # Setup times per category (applied when preceded by different category)
    SETUP_WELDING = 25   # Welding needs 25 min setup
    SETUP_PAINTING = 15  # Painting needs 15 min setup  
    SETUP_ASSEMBLY = 20  # Assembly needs 20 min setup
    
    # Create jobs with due dates and priorities
    # Job D: Simple D parts
    job_d = kr.Job(id="JOB_D_1", name="Product D", task_type="tekerlek",due_date=200, priority=1)
    job_e = kr.Job(id="JOB_D_2", name="Product D", task_type="tekerlek",due_date=220, priority=1)
    
    # Job ABC: All ABC parts + assemblies
    job_abc = kr.Job(id="JOB_ABC", name="Product ABC", due_date=450, priority=2)
    
    # Create tasks (without due_date/priority - they come from Job)
    weld_a = kr.Task(id=101, name="Weld_Part_A", task_type=WELDING, setup_time=SETUP_WELDING)
    weld_a.add_alternative(1, 100)
    weld_a.add_alternative(2, 80)
    weld_a.add_alternative(3, 80)

    paint_a = kr.Task(id=102, name="Paint_Part_A", task_type=PAINTING, setup_time=SETUP_PAINTING)
    paint_a.add_alternative(1, 60)
    paint_a.add_alternative(2, 50)
    paint_a.add_alternative(3, 50)
    paint_a.add_predecessor(weld_a)
    
    weld_b = kr.Task(id=103, name="Weld_Part_B", task_type=WELDING, setup_time=SETUP_WELDING)
    weld_b.add_alternative(1, 90)
    weld_b.add_alternative(2, 70)
    weld_b.add_alternative(3, 70)
    
    paint_b = kr.Task(id=104, name="Paint_Part_B", task_type=PAINTING, setup_time=SETUP_PAINTING)
    paint_b.add_alternative(1, 50)
    paint_b.add_alternative(2, 40)
    paint_b.add_alternative(3, 40)
    paint_b.add_predecessor(weld_b)
    
    assemble_ab = kr.Task(id=105, name="Assemble_A_B", task_type=ASSEMBLY, setup_time=SETUP_ASSEMBLY)
    assemble_ab.add_alternative(1, 120)
    assemble_ab.add_alternative(2, 100)
    assemble_ab.add_alternative(3, 100)
    assemble_ab.add_predecessor(paint_a)
    assemble_ab.add_predecessor(paint_b)
    
    weld_c = kr.Task(id=106, name="Weld_Part_C", task_type=WELDING, setup_time=SETUP_WELDING)
    weld_c.add_alternative(2, 80)
    weld_c.add_alternative(3, 80)
    
    paint_c = kr.Task(id=107, name="Paint_Part_C", task_type=PAINTING, setup_time=SETUP_PAINTING)
    paint_c.add_alternative(2, 50)
    paint_c.add_alternative(3, 50)
    paint_c.add_predecessor(weld_c)
    
    assemble_final = kr.Task(id=108, name="Assemble_Final", task_type=ASSEMBLY, setup_time=SETUP_ASSEMBLY)
    assemble_final.add_alternative(1, 100)
    assemble_final.add_predecessor(assemble_ab)
    assemble_final.add_predecessor(paint_c)
    
    weld_d = kr.Task(id=109_1, name="Weld_Part_D", task_type=WELDING, setup_time=SETUP_WELDING)
    weld_d.add_alternative(2, 10)
    weld_d.add_alternative(3, 10)
    
    paint_d = kr.Task(id=110_1, name="Paint_Part_D", task_type=PAINTING,setup_time=SETUP_PAINTING)
    paint_d.add_alternative(1, 5)
    paint_d.add_predecessor(weld_d)

    weld_e = kr.Task(id=109_2, name="Weld_Part_D", task_type=WELDING, setup_time=SETUP_WELDING)
    weld_e.add_alternative(2, 10)
    weld_e.add_alternative(3, 10)
    
    paint_e = kr.Task(id=110_2, name="Paint_Part_D", task_type=PAINTING,setup_time=SETUP_PAINTING)
    paint_e.add_alternative(1, 5)
    paint_e.add_predecessor(weld_e)

    alone_e = kr.Task(id=111, name="Alone_E", setup_time=15)
    alone_e.add_alternative(1, 5)
    
    # Add tasks to jobs
    # Job D: D parts only
    job_d.add_task(weld_d)
    job_d.add_task(paint_d)

    job_e.add_task(weld_e)
    job_e.add_task(paint_e)
    
    # Job ABC: All ABC parts + assemblies
    job_abc.add_task(weld_a)
    job_abc.add_task(paint_a)
    job_abc.add_task(weld_b)
    job_abc.add_task(paint_b)
    job_abc.add_task(weld_c)
    job_abc.add_task(paint_c)
    job_abc.add_task(assemble_ab)
    job_abc.add_task(assemble_final)

    problem.add_job(job_d)
    problem.add_job(job_e)
    problem.add_job(job_abc)
    problem.add_task(alone_e)
    """

    # parallel tasks to increase complexity (uncomment to use)
    """
    for i in range(6):
        machine = kr.Machine(id=i, name=f"machine_{i}")
        problem.add_machine(machine)

    # Add tasks to problem
    for i in range(5):
        a = 18 // (2+i)
        b = 18 - a
        
        task_copy = kr.Task(id=i, name=f"Alone_Task_{i}", setup_time=10, task_type="Type_A")
        task_copy_2 = kr.Task(id=5+i, name=f"Alone_Task_{5+i}", setup_time=10, task_type="Type_A")
        for m in range(6):
            task_copy.add_alternative(m, a)
            task_copy_2.add_alternative(m, b)
        problem.add_task(task_copy)
        problem.add_task(task_copy_2)

    for i in range(3):
        task_copy_3 = kr.Task(id=10+i, name=f"Alone_Task_{10+i}", setup_time=5, task_type="Type_A")
        for m in range(6):
            task_copy_3.add_alternative(m, 6)
        problem.add_task(task_copy_3)
    """



    print(f"\n📋 Jobs added:")
    for job in problem.jobs:
        print(f"   - {job.name} (due={job.due_date}, priority={job.priority}, tasks={len(job.tasks)})")
    
    print(f"\n📋 Tasks:")
    for task in problem.tasks:
        print(f"   - {task.name} (Type={task.task_type}, Setup={task.setup_time}min, due={task.due_date})")
    """
    print(f"\n🔗 Precedence constraints:")
    print(f"   - {assemble_ab.name} → after {paint_a.name}, {paint_b.name}")
    print(f"   - {assemble_final.name} → after {assemble_ab.name}, {paint_c.name}")
    """
    # Note: Setup times are now per-task, not in a matrix
    print(f"\n⚙️ Setup time logic:")
    print(f"   - Same category → 0 setup")
    print(f"   - Different category → target task's setup_time")
    
    # Analyze problem features
    features = problem.get_features()
    print(f"\n🔍 Problem features detected: {features}")
    
    # Solve using CP-SAT with WEIGHTED_TARDINESS objective
    print(f"\n🚀 Solving with Google CP-SAT...")
    solver = kr.SolverFactory.get_solver(kr.SolverType.CP_SAT, objective_type=kr.ObjectiveType.MAKESPAN, logging_enabled=True)
        
    
    # Check compatibility
    can_solve, msg = solver.can_solve(problem)
    print(f"   Compatibility: {msg}")
    
    result = solver.solve(problem, time_limit_seconds=30)
    
    # Display results
    print(f"\n📊 RESULTS:")
    print(f"   Status: {result.status}")
    print(f"   Solve time: {result.solve_time_seconds:.2f} seconds")
    
    if result.is_success:
        print(f"   {'Total Weighted Tardiness' if result.objective_type == kr.ObjectiveType.WEIGHTED_TARDINESS else 'Makespan'}: {result.objective_value} minutes")
        
        print(f"\n📅 Schedule:")
        print(f"   {'Task':<15} {'Machine':<15} {'Start':>8} {'End':>8} {'Duration':>10}")
        print(f"   {'-'*56}")
        
        for task in result.schedule:
            print(f"   {task.task_name:<15} {task.machine_name:<15} {task.start_time:>8} {task.end_time:>8} {task.duration:>10}")
        
        # Analyze machine assignment for mixed-type jobs
        print(f"\n💡 Analysis:")
        lathe_count = sum(1 for t in result.schedule if t.machine_id == 1)
        cnc_count = sum(1 for t in result.schedule if t.machine_id == 2)
        print(f"   - Manual_Lathe assignments: {lathe_count}")
        print(f"   - CNC_Center assignments: {cnc_count}")
        
        if cnc_count > lathe_count:
            print("   ✅ CNC is preferred due to lower setup times!")
        
        # Visualize (save to HTML)
        try:
            visualizer = kr.GanttVisualizer(color_by="task_type")
            fig = visualizer.draw(result, title="Kairos Demo Schedule")
            fig.write_html("schedule_demo.html")
            print(f"\n📈 Gantt chart saved to: schedule_demo.html")
            
            # Dependency graph (Assembly Chart)
            dep_visualizer = kr.DependencyGraphVisualizer()
            dep_fig = dep_visualizer.draw(problem, title="Task Dependencies (Assembly Chart)")
            dep_fig.write_html("dependencies_demo.html")
            print(f"🔗 Dependency graph saved to: dependencies_demo.html")
        except Exception as e:
            print(f"\n⚠️ Visualization skipped: {e}")
    else:
        print(f"   Message: {result.message}")
    
    print("\n" + "=" * 60)
    print("Demo completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
