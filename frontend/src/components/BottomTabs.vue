<template>
	<ion-tab-bar
		slot="bottom"
		class="bg-white/95 backdrop-blur-md border-t border-slate-200/80 shadow-md py-1.5 pb-2 standalone:pb-safe-bottom"
	>
		<ion-tab-button
			v-for="item in tabItems"
			:key="item.title"
			:tab="item.title"
			:href="item.route"
			:class="[
				'bg-transparent text-[11px] space-y-1 transition active:scale-95',
				route.path === item.route
					? '!text-[#0b1a2d] font-bold'
					: '!text-slate-400 hover:!text-slate-600 font-medium',
			]"
		>
			<div 
				class="p-1 rounded-xl transition-all flex items-center justify-center"
				:class="route.path === item.route ? 'bg-amber-50 text-amber-600 scale-105' : 'text-slate-400'"
			>
				<component :is="item.icon" class="h-5 w-5" />
			</div>
			<div>{{ item.title }}</div>
		</ion-tab-button>
	</ion-tab-bar>
</template>

<script setup>
import { useRoute } from "vue-router"

import { IonTabBar, IonTabButton } from "@ionic/vue"

import HomeIcon from "@/components/icons/HomeIcon.vue"
import LeaveIcon from "@/components/icons/LeaveIcon.vue"
import ExpenseIcon from "@/components/icons/ExpenseIcon.vue"
import SalaryIcon from "@/components/icons/SalaryIcon.vue"
import AttendanceIcon from "@/components/icons/AttendanceIcon.vue"
import { inject } from "vue"

const __ = inject("$translate")

const route = useRoute()

const tabItems = [
	{
		icon: HomeIcon,
		title: __("Home"),
		route: "/home",
	},
	{
		icon: AttendanceIcon,
		title: __("Attendance"),
		route: "/dashboard/attendance",
	},
	{
		icon: LeaveIcon,
		title: __("Leaves"),
		route: "/dashboard/leaves",
	},
	{
		icon: ExpenseIcon,
		title: __("Expenses"),
		route: "/dashboard/expense-claims",
	},
	{
		icon: SalaryIcon,
		title: __("Salary"),
		route: "/dashboard/salary-slips",
	},
]
</script>
